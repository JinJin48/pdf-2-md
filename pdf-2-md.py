#!/usr/bin/env python3
"""
PDF to Markdown Converter

Converts PDF files to structured Markdown.

Usage:
    python pdf-2-md.py                    # Process all PDFs in input_pdf/
    python pdf-2-md.py document.pdf       # Process a single PDF
    python pdf-2-md.py -o output_dir      # Specify output directory
"""

import os
import sys
import shutil
import argparse
import logging
import gc
import time
from pathlib import Path
import pymupdf4llm

from common import (
    INPUT_DIR, OUTPUT_DIR,
    setup_logging, estimate_time, clean_filename,
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


def load_existing_yaml(pdf_path):
    """Load existing YAML metadata file if it exists alongside the PDF."""
    yaml_path = pdf_path.with_suffix('.yaml')
    if yaml_path.exists():
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                content = f.read()
            logging.info(f"Found existing YAML metadata: {yaml_path}")
            return content
        except Exception as e:
            logging.warning(f"Failed to read YAML file {yaml_path}: {e}")
    return None


def save_md(content, pdf_name, output_dir, yaml_content=None):
    """Save markdown content (with optional existing YAML frontmatter)."""
    if yaml_content:
        # Ensure YAML content ends with newlines for proper separation
        if not yaml_content.endswith('\n\n'):
            yaml_content = yaml_content.rstrip('\n') + '\n\n'
        full_content = yaml_content + content
    else:
        full_content = content

    fname = f"{pdf_name}.md"
    fname = clean_filename(fname)

    out_path = Path(output_dir) / fname
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(full_content)
    logging.info(f"Saved: {out_path}")


def main():
    parser = argparse.ArgumentParser(description="PDF to Markdown Converter")
    parser.add_argument("pdf", nargs="?", help="Path to PDF file or directory (optional, uses input_pdf/ if not specified)")
    parser.add_argument("-o", "--output", default=OUTPUT_DIR, help="Output directory for markdown files")
    args = parser.parse_args()

    setup_logging(background_mode=False)
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

        # Load existing YAML metadata if available
        yaml_content = load_existing_yaml(pdf)

        # Save as single MD file
        save_md(processed_content, name, output_dir, yaml_content)
        logging.info(f"Finished processing {name}")

        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)

        processed_count += 1
        estimate_time(start_time, processed_count, total_count)

    logging.info("=== PDF to Markdown Converter Completed ===")


if __name__ == "__main__":
    main()
