#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description='search words file for string')
parser.add_argument('snippet', help='the string to search for in the file')

args = parser.parse_args()

snippet = args.snippet.lower()


with open('words') as f:
    words = f.readlines()

matches = [one_word for one_word in words if snippet in one_word]

print(matches)

