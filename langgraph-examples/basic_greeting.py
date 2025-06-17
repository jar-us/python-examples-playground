"""
Basic LangGraph Example: Simple Greeting
=====================================

This example demonstrates the most basic usage of LangGraph's StateGraph.
It shows how to create a simple one-node graph that processes a name into
a greeting message.

Key Concepts:
-----------
1. State Definition - Using TypedDict
2. Node Creation - Simple transformation function
3. Graph Building - Basic workflow setup
4. Graph Execution - Running with input state

Usage:
-----
python basic_greeting.py

Expected Output:
    Hello, Alice!
"""

from typing import TypedDict
from langgraph.graph import StateGraph, END

class GreetingState(TypedDict):
    """
    Defines the state structure for the greeting workflow.

    Attributes:
        name (str): Input name to be greeted
        message (str): Generated greeting message
    """
    name: str
    message: str

def greet(state: GreetingState) -> dict:
    """
    Creates a greeting message for the given name.

    Args:
        state (GreetingState): Current state containing the name

    Returns:
        dict: Updated state with greeting message

    Example:
        >>> greet({"name": "Bob"})
        {"message": "Hello, Bob!"}
    """
    return {"message": f"Hello, {state['name']}!"}

# Initialize the graph with our state type
workflow = StateGraph(GreetingState)

# Add our greeting function as a node
workflow.add_node("greeter", greet)

# Configure the graph flow:
# Entry point -> greeter node -> end
workflow.set_entry_point("greeter")
workflow.add_edge("greeter", END)

# Compile the graph into a runnable application
app = workflow.compile()

if __name__ == "__main__":
    # Run the graph with an example name
    result = app.invoke({"name": "Alice"})
    print(result["message"])  # Prints: Hello, Alice!

    # Try with a different name
    result = app.invoke({"name": "Bob"})
    print(result["message"])  # Prints: Hello, Bob!
