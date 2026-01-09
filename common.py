import os
import sys
import re
import logging
import time
import datetime
from pathlib import Path

# Configuration
INPUT_DIR = "input_pdf"
OUTPUT_DIR = "output_md"
LOG_FILE = "conversion.log"


def setup_logging(background_mode, log_file=LOG_FILE):
    """Configure logging."""
    handlers = [logging.FileHandler(log_file, encoding='utf-8', mode='a')]
    if not background_mode:
        handlers.append(logging.StreamHandler(sys.stdout))

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=handlers
    )


def estimate_time(start_wall_time, processed_count, total_count):
    """Log estimated completion time."""
    if processed_count == 0:
        return

    elapsed = time.time() - start_wall_time
    avg_per_item = elapsed / processed_count
    remaining = total_count - processed_count
    est_seconds = remaining * avg_per_item

    est_finish = datetime.datetime.now() + datetime.timedelta(seconds=est_seconds)
    logging.info(f"Progress: {processed_count}/{total_count}. "
                 f"Avg: {avg_per_item:.1f}s/item. "
                 f"Est. Finish: {est_finish.strftime('%Y-%m-%d %H:%M:%S')}")


def clean_filename(name):
    """Sanitize filename."""
    return re.sub(r'[\\/*?:"<>|]', "", name)


def remove_pdf_artifacts(md_text):
    """
    Remove PDF artifacts from markdown text:
    - Footer lines (Personal Copy..., © 2025...)
    - Page number markers (**19**, **20**, etc.)
    - Running headers (short unformatted lines with chapter/section numbers)
    """
    lines = md_text.split('\n')
    new_lines = []

    # Patterns to remove
    footer_patterns = [
        re.compile(r'^Personal Copy for .+@.+$', re.IGNORECASE),
        re.compile(r'^©\s*\d{4}\s+by\s+Rheinwerk', re.IGNORECASE),
    ]
    page_number_pattern = re.compile(r'^\*\*\d+\*\*$')

    # Running header: short UNFORMATTED line with just section number and title
    # e.g., "1 Introduction", "1.2 SAP's Data and Analytics Strategy"
    # But NOT formatted lines like "**1.2  SAP's Strategy**" which are actual titles
    running_header_pattern = re.compile(r'^(\d+(?:\.\d+)*)\s+[A-Z].*$')

    for line in lines:
        stripped = line.strip()

        # Skip empty lines
        if not stripped:
            new_lines.append(line)
            continue

        # Remove footer patterns
        skip = False
        for pattern in footer_patterns:
            if pattern.match(stripped):
                skip = True
                break
        if skip:
            continue

        # Remove page number markers
        if page_number_pattern.match(stripped):
            continue

        # Remove running headers (short unformatted lines with section numbers)
        # Running headers are plain text without markdown formatting (**, _, #)
        if running_header_pattern.match(stripped) and len(stripped) < 60:
            # Check if it's unformatted (no bold, italic, or header markers)
            if not stripped.startswith('**') and not stripped.startswith('_') and not stripped.startswith('#'):
                # This is likely a running header, skip it
                continue

        new_lines.append(line)

    return "\n".join(new_lines)


def add_headers_by_pattern(md_text):
    """
    Post-process markdown text to add headers based on numbering patterns.
    Examples:
    "1. Introduction" -> "# 1. Introduction"
    "1.1 Background" -> "## 1.1 Background"

    Only applies to lines that are substantial (>50 chars) to avoid running headers.
    """
    lines = md_text.split('\n')
    new_lines = []

    pattern = re.compile(r'^(\d+(?:\.\d+)*)\s')

    for line in lines:
        if line.strip().startswith('#'):
            new_lines.append(line)
            continue

        match = pattern.match(line.strip())
        if match:
            # Only add header if line is substantial (not a running header)
            if len(line.strip()) > 50:
                num_part = match.group(1)
                dots = num_part.count('.')
                level = min(dots + 1, 6)
                new_line = f"{'#' * level} {line.strip()}"
                new_lines.append(new_line)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)
