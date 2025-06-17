# Python Examples Playground

This repository contains practical examples demonstrating various Python concepts and best practices. Each directory focuses on a specific concept with simple, well-documented examples.

## Current Examples

### 1. LangGraph Examples (`langgraph-examples/`)
Demonstrates the usage of LangGraph from LangChain for creating structured conversation flows:
- Basic greeting workflow
- Two-step processing workflow
- Simple counter example

### 2. Environment Variables (`env-examples/`)
Shows different approaches to handling environment variables in Python applications:
- Basic environment variables usage
- Configuration using classes
- Multiple environment management

## Prerequisites

```bash
# Install required packages
pip install python-dotenv langchain langgraph
```

## Project Structure

```
python-examples-playground/
├── langgraph-examples/
│   ├── hello.py
│   ├── basic_greeting.py
│   ├── two_step.py
│   └── counter.py
│
└── env-examples/
    ├── basic_env.py
    ├── config_class.py
    ├── multiple_env.py
    ├── .env.default
    ├── .env.development
    └── .env.production
```

## Usage

Each directory contains its own README with specific instructions for running the examples. Generally, you can run any example using Python:

```bash
python <directory_name>/<example_name>.py
```

## Documentation

Each example includes:
- Detailed docstrings explaining the purpose and usage
- Comments explaining the code
- README files with comprehensive documentation
- Best practices and considerations

## Contributing

Feel free to:
1. Open issues for questions or problems
2. Submit pull requests for improvements
3. Suggest new examples to add

## License

This project is open source and available under the MIT License.