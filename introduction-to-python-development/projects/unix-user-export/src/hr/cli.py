import sys
from argparse import ArgumentParser, Namespace


def create_parser():
    parser = ArgumentParser

    parser.add_argument(
        '--format',
        type=str.lower(),
        choices=['json', 'csv'],
        default='json',
        help='specify output format: json or csv (default: json)'
    )

    parser.add_argument(
        '--path',
        type=str,
        help='specify path to output file'
    )

    return parser

def main():

