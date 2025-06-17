"""
Configuration Management Example using Environment Variables

This example demonstrates how to create a structured configuration system using
Python's dataclasses and environment variables. It shows:

1. How to organize configuration using dataclasses
2. How to load environment variables into typed configurations
3. How to handle nested configurations (database config within app config)
4. How to provide default values and type safety

Usage:
    python config_class.py

Required Environment Variables:
    None - all variables have defaults

Optional Environment Variables:
    DB_HOST      - Database host (default: localhost)
    DB_PORT      - Database port (default: 5432)
    DB_USER      - Database username (default: postgres)
    DB_PASSWORD  - Database password (default: empty)
    DB_NAME      - Database name (default: myapp)
    DEBUG        - Debug mode flag (default: False)
    PORT         - Application port (default: 8080)
    API_KEY      - API key (default: empty)
    APP_ENV      - Application environment (default: development)

Example .env file:
    DB_HOST=localhost
    DB_PORT=5432
    DB_USER=myuser
    DB_PASSWORD=mypassword
    DEBUG=True
    PORT=8000
"""

from dataclasses import dataclass
from dotenv import load_dotenv
import os
from typing import Optional

# Load environment variables at module level
load_dotenv()

@dataclass
class DatabaseConfig:
    """
    Database configuration container.

    Attributes:
        host (str): Database server hostname
        port (int): Database server port
        username (str): Database user
        password (str): Database password
        database (str): Database name
    """
    host: str
    port: int
    username: str
    password: str
    database: str

@dataclass
class AppConfig:
    """
    Main application configuration container.

    Attributes:
        debug (bool): Debug mode flag
        port (int): Application server port
        database (DatabaseConfig): Database configuration
        api_key (str): API authentication key
        environment (str): Application environment (development/production/etc)
    """
    debug: bool
    port: int
    database: DatabaseConfig
    api_key: str
    environment: str

def load_config() -> AppConfig:
    """
    Load configuration from environment variables with defaults.

    This function creates a hierarchical configuration structure by:
    1. Loading environment variables (already done at module level)
    2. Creating a DatabaseConfig with database-specific variables
    3. Creating an AppConfig containing the DatabaseConfig and app-specific variables

    Returns:
        AppConfig: Complete application configuration with all settings
    """

    # Database configuration
    db_config = DatabaseConfig(
        host=os.getenv('DB_HOST', 'localhost'),
        port=int(os.getenv('DB_PORT', '5432')),
        username=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', ''),
        database=os.getenv('DB_NAME', 'myapp')
    )

    # Application configuration
    app_config = AppConfig(
        debug=os.getenv('DEBUG', 'False').lower() == 'true',
        port=int(os.getenv('PORT', '8080')),
        database=db_config,
        api_key=os.getenv('API_KEY', ''),
        environment=os.getenv('APP_ENV', 'development')
    )

    return app_config

def main():
    """
    Main function to demonstrate configuration loading and usage.

    This function:
    1. Loads the configuration
    2. Prints all non-sensitive configuration values
    3. Masks sensitive values like passwords and API keys
    """
    # Load the configuration
    config = load_config()

    # Print the configuration
    print("=== Application Configuration ===")
    print(f"Environment: {config.environment}")
    print(f"Debug Mode: {config.debug}")
    print(f"Port: {config.port}")
    print(f"API Key: {config.api_key}")

    print("\n=== Database Configuration ===")
    print(f"Host: {config.database.host}")
    print(f"Port: {config.database.port}")
    print(f"Database: {config.database.database}")
    print(f"Username: {config.database.username}")
    print(f"Password: {'*' * len(config.database.password)}")

if __name__ == "__main__":
    main()
