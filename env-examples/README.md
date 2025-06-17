# Environment Variables Examples

This directory contains examples demonstrating different ways to handle environment variables in Python applications using the `python-dotenv` package.

## Prerequisites

```bash
pip install python-dotenv
```

## Examples Overview

### 1. Basic Environment Variables (`basic_env.py`)
The simplest example showing how to:
- Load variables from a `.env` file
- Access environment variables with default values
- Handle missing variables

### 2. Configuration Class (`config_class.py`)
Demonstrates structured configuration management using:
- Python dataclasses for type safety
- Hierarchical configuration structure
- Organized configuration groups (database, app settings)

### 3. Multiple Environments (`multiple_env.py`)
Shows how to manage multiple environment configurations:
- Load different configs based on environment (dev, prod, etc.)
- Implement configuration inheritance
- Handle configuration overrides

## Environment Files

### Structure
- `.env` - Local environment overrides (not in version control)
- `.env.default` - Default configuration (in version control)
- `.env.development` - Development environment settings
- `.env.production` - Production environment settings

### Loading Order
1. `.env.default` (base settings)
2. `.env.{environment}` (environment-specific settings)
3. `.env` (local overrides)

## Best Practices Demonstrated

1. **Security**
   - Keep sensitive information in environment variables
   - Never commit actual secrets to version control
   - Use `.env.example` or `.env.default` as templates

2. **Configuration Management**
   - Use meaningful variable names
   - Provide default values for optional settings
   - Implement environment-specific configurations

3. **Code Organization**
   - Separate configuration from application logic
   - Use type hints for better maintainability
   - Follow the principle of least surprise

## Running the Examples

Each example can be run directly:

```bash
# Basic example
python basic_env.py

# Configuration class example
python config_class.py

# Multiple environments example
python multiple_env.py
```

## Example .env File

Here's a sample `.env` file demonstrating common variables:

```ini
# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/mydb

# API Configuration
API_KEY=your_secret_key_here

# Application Settings
DEBUG=True
PORT=8080
APP_ENV=development
```

## Further Reading

- [python-dotenv Documentation](https://github.com/theskumar/python-dotenv)
- [12 Factor App - Config](https://12factor.net/config)
- [Python Documentation - os.environ](https://docs.python.org/3/library/os.html#os.environ)