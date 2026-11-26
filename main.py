#!/usr/bin/env python3
"""Read output/entry.txt and print its contents."""
from pathlib import Path

def main():
    entry = Path(__file__).resolve().parent / "output" / "entry.txt"
    print(entry.read_text(encoding="utf-8").strip())

if __name__ == "__main__":
    main()
