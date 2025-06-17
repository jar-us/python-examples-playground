# LangGraph Examples

This directory contains examples demonstrating the usage of LangGraph from LangChain. Each example shows different aspects of building workflows using StateGraph.

## Prerequisites

```bash
pip install langgraph
```

## Examples Overview

### 1. Basic Greeting (`basic_greeting.py`)
The simplest example showing how to:
- Create a basic StateGraph
- Define state using TypedDict
- Create a single node workflow
- Process input to output

### 2. Two-Step Processing (`two_step.py`)
Demonstrates a two-node workflow:
- Connect multiple nodes in sequence
- Pass state between nodes
- Transform data through multiple steps
- Chain operations together

### 3. Counter (`counter.py`)
Shows simple state transformation:
- Basic numeric processing
- Minimal state management
- Single node with state update
- Simple input/output flow

## Files Structure

```
langgraph-examples/
├── README.md
├── basic_greeting.py     # Basic one-node example
├── two_step.py          # Two-node sequential workflow
└── counter.py           # Simple state transformation
```

## Running the Examples

Each example can be run independently:

```bash
# Run basic greeting example
python basic_greeting.py

# Run two-step processing example
python two_step.py

# Run counter example
python counter.py
```

## Key Concepts Demonstrated

1. **State Management**
   - Using TypedDict for state definition
   - Passing state between nodes
   - Updating state in nodes

2. **Graph Construction**
   - Creating nodes
   - Defining edges
   - Setting entry/exit points

3. **Workflow Patterns**
   - Single node processing
   - Sequential processing
   - State transformation

## Best Practices Shown

1. **Code Organization**
   - Clear state definitions
   - Well-documented functions
   - Logical workflow structure

2. **Error Handling**
   - Type safety with TypedDict
   - Default value handling
   - State validation

3. **Documentation**
   - Comprehensive docstrings
   - Usage examples
   - Clear code comments

## Further Reading

- [LangGraph Documentation](https://python.langchain.com/docs/langgraph)
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)