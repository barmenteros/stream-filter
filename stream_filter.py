#!/usr/bin/env python3
"""
stream_filter.py

Reads a (potentially huge) text file line by line, and writes out only
those lines that contain a given substring (case-sensitive). It will:
  1) Try your system default encoding first.
  2) If no matches, fall back to UTF-16 LE (handles BOM).
  3) Report how many lines were written, or error if none found.

Usage:
    python stream_filter.py /path/to/log.txt "AUDUSD,M15"
"""

import argparse
import os
import sys

def build_output_path(input_path: str, suffix: str = "_filtered") -> str:
    directory, filename = os.path.split(input_path)
    name, ext = os.path.splitext(filename)
    if not ext:
        ext = ".txt"
    return os.path.join(directory, f"{name}{suffix}{ext}")

def filter_file(input_path: str, output_path: str, substring: str):
    """
    Attempt filtering with default encoding, then UTF-16 LE if no hits.
    """
    def _scan_and_write(enc, mode):
        count = 0
        with open(input_path, 'r', encoding=enc, errors='replace') as src, \
             open(output_path, mode, encoding='utf-8') as dst:
            for line in src:
                if substring in line:
                    dst.write(line)
                    count += 1
        return count

    # First pass: system default (encoding=None)
    matches = _scan_and_write(None, 'w')
    if matches > 0:
        return matches

    # Second pass: UTF-16 LE (auto‐detect BOM)
    matches = _scan_and_write('utf-16', 'w')
    if matches > 0:
        return matches

    # Nothing matched
    sys.exit(f"❗ No lines containing '{substring}' were found. "
             "Please verify the substring and/or the file’s encoding.")

def parse_args():
    p = argparse.ArgumentParser(
        description="Stream-filter a large text file by simple substring match."
    )
    p.add_argument("input_file", help="Path to the source log file")
    p.add_argument("filter_string", help="Case-sensitive substring to match")
    return p.parse_args()

def main():
    args = parse_args()
    inp = args.input_file
    substr = args.filter_string
    outp = build_output_path(inp)

    print(f"Scanning '{inp}' for lines containing '{substr}' …")
    matches = filter_file(inp, outp, substr)
    print(f"✅ Done: {matches} matching lines written to '{outp}'")

if __name__ == "__main__":
    main()
