"""
Multiple Environment Configuration Example
=======================================

This example demonstrates how to manage multiple environment configurations
in a Python application. It shows:

1. Loading different .env files based on the environment (dev, test, prod)
2. Using a hierarchy of environment files
3. Implementing environment-specific configurations
4. Handling configuration overrides

File Hierarchy:
-------------
.env.default   - Base configuration, checked into version control
.env.{env}     - Environment-specific configuration (development, testing, production)
.env           - Local overrides, not checked into version control

Loading Order:
------------
1. .env.default (base settings)
2. .env.{environment} (environment-specific settings)
3. .env (local overrides)

Usage:
-----
1. Create environment files:
   - .env.default
   - .env.development
   - .env.production

2. Run the script:
   python multiple_env.py

Requirements:
-----------
- python-dotenv package: pip install python-dotenv
"""

from dotenv import load_dotenv
import os
from pathlib import Path

def load_environment(env_name: str = 'development'):
    """
    Load environment variables from multiple .env files.

    This function implements a hierarchical configuration system where:
    1. Base defaults are loaded first (.env.default)
    2. Environment-specific settings override defaults (.env.{environment})
    3. Local settings have highest precedence (.env)

    Args:
        env_name (str): Name of the environment to load (default: 'development')
                       Common values: 'development', 'testing', 'production'

    Example:
        >>> load_environment('development')
        Loaded default environment from .env.default
        Loaded development environment from .env.development
        Loaded local overrides from .env
    """

    # Get the directory containing the .env files
    env_path = Path(__file__).parent

    # Load default variables first
    default_env = env_path / '.env.default'
    if default_env.exists():
        load_dotenv(default_env)
        print(f"Loaded default environment from {default_env}")

    # Load environment-specific variables
    env_file = env_path / f'.env.{env_name}'
    if env_file.exists():
        load_dotenv(env_file, override=True)
        print(f"Loaded {env_name} environment from {env_file}")

    # Load local overrides last
    local_env = env_path / '.env'
    if local_env.exists():
        load_dotenv(local_env, override=True)
        print(f"Loaded local overrides from {local_env}")

def get_config():
    """
    Get the current configuration values from environment.

    Returns:
        dict: Dictionary containing current configuration values:
            - environment: Current environment name
            - debug: Debug mode flag
            - database_url: Database connection string
            - api_key: API authentication key
            - port: Application port

    Note:
        Sensitive values like api_key will be masked when printed
    """
    return {
        'environment': os.getenv('APP_ENV', 'development'),
        'debug': os.getenv('DEBUG', 'False').lower() == 'true',
        'database_url': os.getenv('DATABASE_URL', 'default_db_url'),
        'api_key': os.getenv('API_KEY', 'default_key'),
        'port': int(os.getenv('PORT', '8080'))
    }

def main():
    """
    Demonstrate loading and using multiple environment configurations.

    This function:
    1. Loads each environment configuration in sequence
    2. Displays the resulting configuration for each environment
    3. Shows how values override each other based on precedence
    """
    # Example: Load different environments
    environments = ['development', 'testing', 'production']

    for env in environments:
        print(f"\n=== Loading {env} environment ===")
        load_environment(env)

        # Print current configuration
        config = get_config()
        print("\nCurrent Configuration:")
        for key, value in config.items():
            # Mask sensitive values
            if 'key' in key.lower() or 'password' in key.lower():
                print(f"{key}: {'*' * 8}")
            else:
                print(f"{key}: {value}")

if __name__ == "__main__":
    main()
