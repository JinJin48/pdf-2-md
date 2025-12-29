#!/usr/bin/env python3
"""
PDF to Dify-ready Markdown Converter

Converts PDF files to structured Markdown with YAML frontmatter,
optimized for Dify knowledge base ingestion.

Usage:
    python pdf-converter-4-dify.py                    # Process all PDFs in input_pdf/
    python pdf-converter-4-dify.py document.pdf      # Process a single PDF
    python pdf-converter-4-dify.py -t "tag1,tag2"    # Specify tags
    python pdf-converter-4-dify.py --background      # Run without GUI prompts
"""

import os
import sys
import shutil
import argparse
import logging
import re
import gc
import time
import tkinter as tk
from tkinter import simpledialog
from pathlib import Path
import pymupdf4llm

from common import (
    INPUT_DIR, OUTPUT_DIR, INTERMEDIATE_DIR, MAX_FILE_SIZE_BYTES,
    setup_logging, load_progress, save_progress,
    estimate_time, clean_filename, get_yaml_header, add_headers_by_pattern
)


class MarkdownSplitter:
    def __init__(self, content, pdf_name, tags, output_base):
        self.content = content
        self.pdf_name = pdf_name
        self.tags = tags
        self.output_base = Path(output_base)
        self.lines = content.split('\n')
        self.toc_content = ""
        self.parts = []

    def split_structured(self):
        """
        Structured split based on headers and size.
        1. Extract Contents -> [PDF]_0_Contents.md
        2. Split by Chapter (# or ##) -> [PDF]_[Num].md
        3. If > 14MB -> Split by Section -> [PDF]_[Num].[Sub].md
        """
        lines = self.lines

        h1_count = sum(1 for line in lines if line.startswith("# "))
        h2_count = sum(1 for line in lines if line.startswith("## "))

        root_level = 1
        if h1_count < 3 and h2_count > 3:
            root_level = 2

        def get_level(line):
            if line.startswith("### "):
                return 3
            if line.startswith("## "):
                return 2
            if line.startswith("# "):
                return 1
            return 0

        nodes = []
        curr_lines = []
        curr_head = "Frontmatter"
        curr_lvl = 0

        for line in lines:
            lvl = get_level(line)
            if lvl > 0 and lvl <= root_level + 2:
                if curr_lines:
                    nodes.append({'lvl': curr_lvl, 'header': curr_head, 'lines': curr_lines})

                curr_lines = [line]
                curr_head = line.strip().lstrip("#").strip()
                curr_lvl = lvl
            else:
                curr_lines.append(line)

        if curr_lines:
            nodes.append({'lvl': curr_lvl, 'header': curr_head, 'lines': curr_lines})

        groups = []
        current_group = None

        contents_node = None

        for node in nodes:
            if re.search(r'^(Table of )?Contents', node['header'], re.IGNORECASE):
                contents_node = node
                continue

            is_chapter = (node['lvl'] == root_level)

            if is_chapter:
                current_group = {'node': node, 'children': []}
                groups.append(current_group)
            elif current_group:
                current_group['children'].append(node)
            else:
                if not groups:
                    groups.append({'node': {'lvl': 0, 'header': 'Frontmatter', 'lines': []}, 'children': []})
                groups[0]['children'].append(node)

        if contents_node:
            self.save_part(contents_node['lines'], "0_Contents", "Table of Contents", "0")

        for group in groups:
            header = group['node']['header']
            match = re.match(r'^(\d+)(\.\d+)*\s+', header)
            if match:
                chap_num = match.group(0).strip()
            else:
                chap_num = clean_filename(header)[:30]

            full_lines = group['node']['lines'][:]
            for child in group['children']:
                full_lines.extend(child['lines'])

            text = "\n".join(full_lines)
            size = len(text.encode('utf-8'))

            if size <= MAX_FILE_SIZE_BYTES:
                self.save_part(full_lines, f"{chap_num}", header, chap_num)
            else:
                self.save_part(group['node']['lines'], f"{chap_num}_Intro", header, chap_num)

                sub_groups = []
                curr_sub = None

                for child in group['children']:
                    if child['lvl'] == root_level + 1:
                        curr_sub = {'node': child, 'children': []}
                        sub_groups.append(curr_sub)
                    elif curr_sub:
                        curr_sub['children'].append(child)
                    else:
                        curr_sub = {'node': {'lvl': root_level + 1, 'header': f"{header} - Part 1", 'lines': []}, 'children': []}
                        sub_groups.append(curr_sub)
                        curr_sub['children'].append(child)

                for sub in sub_groups:
                    sub_header = sub['node']['header']
                    sub_match = re.match(r'^(\d+(\.\d+)+)\s+', sub_header)
                    if sub_match:
                        sub_num = sub_match.group(1).strip()
                    else:
                        sub_num = f"{chap_num}_{clean_filename(sub_header)[:20]}"

                    sub_lines = sub['node']['lines'][:]
                    for c in sub['children']:
                        sub_lines.extend(c['lines'])

                    sub_text = "\n".join(sub_lines)
                    sub_size = len(sub_text.encode('utf-8'))

                    if sub_size <= MAX_FILE_SIZE_BYTES:
                        self.save_part(sub_lines, sub_num, sub_header, sub_num)
                    else:
                        self.save_part(sub['node']['lines'], f"{sub_num}_intro", sub_header, sub_num)

                        for subsub_node in sub['children']:
                            ss_header = subsub_node['header']
                            ss_match = re.match(r'^(\d+(\.\d+)+)\s+', ss_header)
                            if ss_match:
                                ss_num = ss_match.group(1).strip()
                            else:
                                ss_num = f"{sub_num}_{clean_filename(ss_header)[:20]}"

                            ss_lines = subsub_node['lines']
                            ss_size = len("\n".join(ss_lines).encode('utf-8'))

                            if ss_size <= MAX_FILE_SIZE_BYTES:
                                self.save_part(ss_lines, ss_num, ss_header, ss_num)
                            else:
                                self.save_serial_chunks(ss_lines, ss_num, ss_header)

    def save_serial_chunks(self, lines, base_name, title):
        CHUNK_SIZE = 5000
        for i in range(0, len(lines), CHUNK_SIZE):
            chunk = lines[i:i + CHUNK_SIZE]
            num = i // CHUNK_SIZE + 1
            suffix = f"{base_name}_{num:03d}"
            self.save_part(chunk, suffix, f"{title} (Part {num})", base_name)

    def save_part(self, lines, suffix, title, chapter_num):
        yaml = get_yaml_header(self.tags, self.pdf_name + ".pdf", chapter_num, title)
        content = yaml + "\n".join(lines)

        fname = f"{self.pdf_name}_{suffix}.md".replace("..", ".")
        fname = clean_filename(fname)

        out_path = self.output_base / fname
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(content)
        logging.info(f"Saved: {out_path}")


def convert_pdf_to_md(pdf_path, temp_output_dir):
    """Convert PDF to markdown using pymupdf4llm with simple call + post-processing."""
    logging.info(f"Converting {pdf_path} using pymupdf4llm...")

    try:
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path),
            write_images=True,
            image_path=str(temp_output_dir)
        )

        md_text = add_headers_by_pattern(md_text)

        out_name = pdf_path.stem + ".md"
        out_path = temp_output_dir / out_name
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_text)

        return True

    except Exception as e:
        logging.error(f"Error converting PDF with pymupdf4llm: {e}")
        import traceback
        logging.error(traceback.format_exc())
        return False


def get_metadata_from_user(pdf_name, background_mode=False):
    """Popup GUI to get tags."""
    if background_mode:
        logging.info(f"Background mode: Skipping metadata input for '{pdf_name}' (using default/empty).")
        return ""

    root = tk.Tk()
    root.withdraw()

    tags = simpledialog.askstring(
        "Metadata Input",
        f"Enter tags for '{pdf_name}' (comma separated):\nExample: SAC, Analytics, BW"
    )

    root.destroy()
    return tags if tags else ""


def main():
    parser = argparse.ArgumentParser(description="PDF to Dify-ready Markdown Converter")
    parser.add_argument("pdf", nargs="?", help="Path to PDF file or directory (optional, uses input_pdf/ if not specified)")
    parser.add_argument("-o", "--output", default=OUTPUT_DIR, help="Output directory for markdown files")
    parser.add_argument("-t", "--tags", default="", help="Tags for metadata (comma separated)")
    parser.add_argument("--background", action="store_true", help="Run in background mode (no GUI prompts)")
    args = parser.parse_args()

    setup_logging(args.background)
    logging.info("=== PDF to Markdown Converter Started ===")

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.pdf:
        pdf_path = Path(args.pdf)
        if pdf_path.is_dir():
            pdfs = list(pdf_path.glob("*.pdf"))
        else:
            pdfs = [pdf_path]
    else:
        input_path = Path(INPUT_DIR)
        if not input_path.exists():
            input_path.mkdir(exist_ok=True)
        pdfs = list(input_path.glob("*.pdf"))

    if not pdfs:
        logging.warning("No PDFs found to process.")
        return

    progress = load_progress()
    perm_intermediate_dir = Path(INTERMEDIATE_DIR)
    perm_intermediate_dir.mkdir(exist_ok=True)

    start_time = time.time()
    processed_count = 0
    total_count = len(pdfs)

    for pdf in pdfs:
        name = pdf.stem
        logging.info(f"Processing: {name}")

        if name in progress and progress[name].get("status") == "done":
            logging.info(f"Skipping {name} (already marked as done).")
            processed_count += 1
            estimate_time(start_time, processed_count, total_count)
            continue

        if args.tags:
            tags = args.tags
        else:
            tags = get_metadata_from_user(name, args.background)

        temp_dir = Path("temp_conversion_out")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        temp_dir.mkdir()

        if name not in progress:
            progress[name] = {"status": "in_progress", "completed_chunks": []}

        chunk_id = f"{name}_main"
        chunk_perm_md = perm_intermediate_dir / f"{chunk_id}.md"

        if chunk_id in progress[name]["completed_chunks"] and chunk_perm_md.exists():
            logging.info(f"Resuming: Found existing completed conversion for {name}.")
            with open(chunk_perm_md, "r", encoding="utf-8") as f:
                full_content = f.read()
        else:
            chunk_temp_out = temp_dir / "main"
            chunk_temp_out.mkdir(parents=True, exist_ok=True)

            try:
                res = convert_pdf_to_md(pdf, chunk_temp_out)
                if not res:
                    logging.error(f"Failed to convert {name}. Skipping.")
                    continue
            except Exception as e:
                logging.error(f"Exception during conversion of {name}: {e}. Skipping.")
                continue
            finally:
                gc.collect()

            md_files = list(chunk_temp_out.rglob("*.md"))
            if not md_files:
                logging.error(f"No MD found for {name}.")
                continue

            part_md = md_files[0]
            with open(part_md, "r", encoding="utf-8") as f:
                raw_content = f.read()

            img_out_dir = output_dir / "images"
            if not img_out_dir.exists():
                img_out_dir.mkdir(parents=True)

            processed_content = raw_content
            for img in chunk_temp_out.rglob("*"):
                if img.suffix.lower() in ['.png', '.jpg', '.jpeg']:
                    new_img_name = f"{name}_{img.name}"
                    dest_img = img_out_dir / new_img_name
                    shutil.copy(img, dest_img)
                    processed_content = processed_content.replace(img.name, f"images/{new_img_name}")

            full_content = processed_content

            with open(chunk_perm_md, "w", encoding="utf-8") as f:
                f.write(full_content)

            progress[name]["completed_chunks"].append(chunk_id)
            save_progress(progress)

        logging.info("Splitting and parsing content...")
        splitter = MarkdownSplitter(full_content, name, tags, output_dir)
        splitter.split_structured()
        logging.info(f"Finished processing {name}")

        progress[name]["status"] = "done"
        save_progress(progress)

        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)

        processed_count += 1
        estimate_time(start_time, processed_count, total_count)

    logging.info("=== PDF to Markdown Converter Completed ===")


if __name__ == "__main__":
    main()
