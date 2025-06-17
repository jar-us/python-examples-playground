"""
Basic Environment Variables Example
=================================

This script demonstrates the basic usage of environment variables in Python
using the python-dotenv package. It shows the fundamental concepts of:

1. Loading environment variables from a .env file
2. Accessing environment variables with default values
3. Basic error handling for missing variables

Features Demonstrated:
-------------------
- Loading .env files
- Reading environment variables
- Setting default values
- Checking variable existence

Required Environment Variables:
----------------------------
None - all variables have defaults

Optional Environment Variables:
---------------------------
- DATABASE_URL: Database connection string
- API_KEY: API authentication key
- DEBUG: Debug mode flag (True/False)

Example .env file:
----------------
DATABASE_URL=postgresql://user:pass@localhost:5432/db
API_KEY=your_secret_key_123
DEBUG=True

Usage:
-----
1. Create a .env file with desired variables
2. Run: python basic_env.py

Note: This is a basic example. For production use, consider:
- Using a configuration class
- Implementing type validation
- Adding error handling
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_database_url() -> str:
    """
    Get the database URL from environment variables.

    Returns:
        str: The database URL or default value if not set

    Example:
        >>> get_database_url()
        'postgresql://user:pass@localhost:5432/db'
    """
    return os.getenv('DATABASE_URL', 'default_db_url')

def get_api_key() -> str:
    """
    Get the API key from environment variables.

    Returns:
        str: The API key or default value if not set
    """
    return os.getenv('API_KEY', 'default_api_key')

def is_debug_mode() -> bool:
    """
    Check if debug mode is enabled.

    Returns:
        bool: True if DEBUG environment variable exists
    """
    return bool(os.getenv('DEBUG'))

def main():
    """
    Main function demonstrating how to access environment variables.
    Shows different ways to read variables and handle missing values.

    This function demonstrates:
    1. Reading variables with default values
    2. Checking for variable existence
    3. Basic formatting and display of values
    """
    # Get environment variables
    database_url = get_database_url()
    api_key = get_api_key()

    print("=== Environment Variables ===")
    print(f"Database URL: {database_url}")
    print(f"API Key: {api_key}")

    # Show how to check if an env variable exists
    if is_debug_mode():
        print("\nDebug mode is enabled!")
    else:
        print("\nDebug mode is disabled!")

if __name__ == "__main__":
    print(__doc__)  # Print the module documentation
    main()
