import os
import sys
import re
import logging
import json
import time
import datetime
from pathlib import Path

# Configuration
INPUT_DIR = "input_pdf"
OUTPUT_DIR = "output_md"
LOG_FILE = "conversion.log"
PROGRESS_FILE = "progress.json"
INTERMEDIATE_DIR = "intermediate_chunks"
MAX_FILE_SIZE_BYTES = 14 * 1024 * 1024  # 14MB


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


def load_progress(progress_file=PROGRESS_FILE):
    """Load progress from json."""
    if os.path.exists(progress_file):
        try:
            with open(progress_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return {}
    return {}


def save_progress(progress_data, progress_file=PROGRESS_FILE):
    """Save progress to json."""
    with open(progress_file, 'w', encoding='utf-8') as f:
        json.dump(progress_data, f, indent=2, ensure_ascii=False)


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


def get_yaml_header(tags, source, chapter, title):
    """Generate YAML frontmatter."""
    tag_list = [t.strip() for t in tags.split(",") if t.strip()]

    yaml = "---\n"
    yaml += "tags:\n"
    for t in tag_list:
        yaml += f"  - {t}\n"
    yaml += f"source: {source}\n"
    if chapter:
        yaml += f"chapter: {chapter}\n"
    if title:
        yaml += f"title: {title}\n"
    yaml += "---\n\n"
    return yaml


def add_headers_by_pattern(md_text):
    """
    Post-process markdown text to add headers based on numbering patterns.
    Examples:
    "1. Introduction" -> "# 1. Introduction"
    "1.1 Background" -> "## 1.1 Background"
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
            num_part = match.group(1)
            dots = num_part.count('.')
            level = min(dots + 1, 6)
            new_line = f"{'#' * level} {line.strip()}"
            new_lines.append(new_line)
        else:
            new_lines.append(line)

    return "\n".join(new_lines)
