#!/usr/bin/env python3
"""
stream_delete.py

Reads a (potentially huge) text file line by line, and writes out only
those lines that DO NOT contain a given substring (case-sensitive). It will:
  1) Try your system default encoding first.
  2) If no matches to delete, fall back to UTF-16 LE (handles BOM).
  3) Report how many lines were kept (deleted lines excluded).

Usage:
    python stream_delete.py /path/to/log.txt "ERROR"
"""

import argparse
import os
import sys

def build_output_path(input_path: str, suffix: str = "_cleaned") -> str:
    directory, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    if not ext:
        ext = ".txt"
    return os.path.join(directory, f"{name}{suffix}{ext}")

def delete_filter_file(input_path: str, output_path: str, substring: str):
    """
    Attempt filtering with default encoding, then UTF-16 LE if no hits.
    Writes lines that DO NOT contain the substring.
    """
    def _scan_and_write(enc, mode):
        kept_count = 0
        deleted_count = 0
        with open(input_path, 'r', encoding=enc, errors='replace') as src, \
             open(output_path, mode, encoding='utf-8') as dst:
            for line in src:
                if substring not in line:
                    dst.write(line)
                    kept_count += 1
                else:
                    deleted_count += 1
        return kept_count, deleted_count

    # First pass: system default (encoding=None)
    kept, deleted = _scan_and_write(None, 'w')
    if deleted > 0:
        return kept, deleted

    # Second pass: UTF-16 LE (auto-detect BOM)
    kept, deleted = _scan_and_write('utf-16', 'w')
    if deleted > 0:
        return kept, deleted

    # Nothing to delete (substring not found)
    sys.exit(f"❗ No lines containing '{substring}' were found. "
             "The output file contains all lines from the input.")

def parse_args():
    p = argparse.ArgumentParser(
        description="Stream-delete lines from a large text file by simple substring match."
    )
    p.add_argument("input_file", help="Path to the source log file")
    p.add_argument("filter_string", help="Case-sensitive substring to delete")
    return p.parse_args()

def main():
    args = parse_args()
    inp = args.input_file
    substr = args.filter_string
    outp = build_output_path(inp)

    print(f"Scanning '{inp}' to delete lines containing '{substr}' …")
    kept, deleted = delete_filter_file(inp, outp, substr)
    print(f"✅ Done: {deleted} lines deleted, {kept} lines kept and written to '{outp}'")

if __name__ == "__main__":
    main()
