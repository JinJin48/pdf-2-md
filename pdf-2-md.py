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
    python pdf-converter-4-dify.py --background -b "SAP_Analytics_Cloud"  # With book title
"""

import os
import sys
import shutil
import argparse
import logging
import gc
import time
import tkinter as tk
from tkinter import simpledialog
from pathlib import Path
import pymupdf4llm

from common import (
    INPUT_DIR, OUTPUT_DIR,
    setup_logging, estimate_time, clean_filename, get_yaml_header,
    remove_pdf_artifacts, add_headers_by_pattern
)


def convert_pdf_to_md(pdf_path, temp_output_dir):
    """Convert PDF to markdown using pymupdf4llm with simple call + post-processing."""
    logging.info(f"Converting {pdf_path} using pymupdf4llm...")

    try:
        md_text = pymupdf4llm.to_markdown(
            str(pdf_path),
            write_images=True,
            image_path=str(temp_output_dir)
        )

        # Post-processing: remove artifacts then add headers
        md_text = remove_pdf_artifacts(md_text)
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


def save_with_yaml(content, pdf_name, tags, output_dir, book_title=""):
    """Save markdown content with YAML frontmatter (1 PDF = 1 MD file)."""
    yaml_header = get_yaml_header(tags, pdf_name + ".pdf", "", pdf_name)
    full_content = yaml_header + content

    # Add book title prefix if provided
    if book_title:
        fname = f"{book_title}_{pdf_name}.md"
    else:
        fname = f"{pdf_name}.md"
    fname = clean_filename(fname)

    out_path = Path(output_dir) / fname
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    logging.info(f"Saved: {out_path}")


def get_book_title_from_user(background_mode=False):
    """Popup GUI to get book title (called once at start)."""
    if background_mode:
        logging.info("Background mode: Skipping book title input.")
        return ""

    root = tk.Tk()
    root.withdraw()

    book_title = simpledialog.askstring(
        "Book Title Input",
        "Enter the book title (will be prefixed to all output files):\nExample: SAP_Analytics_Cloud"
    )

    root.destroy()
    return book_title if book_title else ""


def get_tags_from_user(background_mode=False):
    """Popup GUI to get tags (called once at start)."""
    if background_mode:
        logging.info("Background mode: Skipping tags input (using default/empty).")
        return ""

    root = tk.Tk()
    root.withdraw()

    tags = simpledialog.askstring(
        "Metadata Input",
        "Enter tags for all PDFs (comma separated):\nExample: SAC, Analytics, BW"
    )

    root.destroy()
    return tags if tags else ""


def main():
    parser = argparse.ArgumentParser(description="PDF to Dify-ready Markdown Converter")
    parser.add_argument("pdf", nargs="?", help="Path to PDF file or directory (optional, uses input_pdf/ if not specified)")
    parser.add_argument("-o", "--output", default=OUTPUT_DIR, help="Output directory for markdown files")
    parser.add_argument("-t", "--tags", default="", help="Tags for metadata (comma separated)")
    parser.add_argument("-b", "--book", default="", help="Book title to prefix all output filenames")
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

    # Get book title once at the start (applies to all PDFs)
    if args.book:
        book_title = args.book
    else:
        book_title = get_book_title_from_user(args.background)

    # Get tags once at the start (applies to all PDFs)
    if args.tags:
        tags = args.tags
    else:
        tags = get_tags_from_user(args.background)

    start_time = time.time()
    processed_count = 0
    total_count = len(pdfs)

    for pdf in pdfs:
        name = pdf.stem
        logging.info(f"Processing: {name}")

        temp_dir = Path("temp_conversion_out")
        if temp_dir.exists():
            shutil.rmtree(temp_dir)
        temp_dir.mkdir()

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

        # Save as single MD file with YAML frontmatter
        save_with_yaml(processed_content, name, tags, output_dir, book_title)
        logging.info(f"Finished processing {name}")

        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)

        processed_count += 1
        estimate_time(start_time, processed_count, total_count)

    logging.info("=== PDF to Markdown Converter Completed ===")


if __name__ == "__main__":
    main()
