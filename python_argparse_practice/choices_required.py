#!/usr/bin/env python3
"""
Example showing required arguments and choices in argparse.

Example usage:
    python choices_required.py --color red --size large
    python choices_required.py --color blue --size medium
"""

import argparse

def main():
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description='Demonstrating required arguments and choices'
    )

    # Required argument with choices
    parser.add_argument(
        '--color',
        required=True,
        choices=['red', 'blue', 'green'],
        help='Select a color (required)'
    )

    # Required argument with choices
    parser.add_argument(
        '--size',
        required=True,
        choices=['small', 'medium', 'large'],
        help='Select a size (required)'
    )

    # Parse arguments
    args = parser.parse_args()

    # Print the selected options
    print(f"You selected:")
    print(f"Color: {args.color}")
    print(f"Size: {args.size}")

if __name__ == '__main__':
    main()
