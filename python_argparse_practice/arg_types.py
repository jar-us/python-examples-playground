#!/usr/bin/env python3
"""
Example showing different argument types in argparse.

Example usage:
    python arg_types.py 42 3.14 --words hello world --flag
"""

import argparse

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='Demonstrating different argument types')

    # Integer type
    parser.add_argument(
        'number',
        type=int,
        help='An integer number'
    )

    # Float type
    parser.add_argument(
        'decimal',
        type=float,
        help='A decimal number'
    )

    # List of strings (nargs)
    parser.add_argument(
        '--words',
        nargs='+',  # One or more arguments
        help='One or more words'
    )

    # Boolean flag
    parser.add_argument(
        '--flag',
        action='store_true',
        help='A boolean flag'
    )

    # Parse arguments
    args = parser.parse_args()

    # Print the values and their types
    print(f"Integer: {args.number} (type: {type(args.number)})")
    print(f"Float: {args.decimal} (type: {type(args.decimal)})")

    if args.words:
        print(f"Words: {args.words} (type: {type(args.words)})")

    print(f"Flag: {args.flag} (type: {type(args.flag)})")

if __name__ == '__main__':
    main()
