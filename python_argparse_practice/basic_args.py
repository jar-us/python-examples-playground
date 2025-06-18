#!/usr/bin/env python3
"""
Basic example of argparse showing positional and optional arguments.

Example usage:
    python basic_args.py John --greeting Hello
    python basic_args.py Alice
"""

import argparse

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(description='A simple greeting program')

    # Add a positional argument (required)
    parser.add_argument('name', help='Name of the person to greet')

    # Add an optional argument with a default value
    parser.add_argument('--greeting', default='Hi', help='The greeting to use (default: Hi)')

    # Parse the arguments
    args = parser.parse_args()

    # Use the arguments
    print(f"{args.greeting}, {args.name}!")

if __name__ == '__main__':
    main()
