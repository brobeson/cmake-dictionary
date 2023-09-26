#!/usr/bin/env python3

"""Sort each group of words in the word list."""

with open("unsorted_words.txt", encoding="utf-8", mode="r") as f:
    all_lines = [l.strip() for l in f.readlines()]
all_lines = sorted(list(set(all_lines)))
with open("unsorted_words.txt", encoding="utf-8", mode="w") as f:
    for l in all_lines:
        f.write(f"{l}\n")
