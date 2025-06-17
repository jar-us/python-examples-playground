"""
Two-Step LangGraph Example: Number Processing
=========================================

This example demonstrates a two-node workflow using LangGraph's StateGraph.
It shows how to:
1. Process data through multiple steps
2. Pass state between nodes
3. Chain operations together

Key Concepts:
-----------
1. Multi-Node Workflow
   - Sequential processing
   - State passing between nodes
   - Node communication

2. State Management
   - Accumulating state changes
   - Accessing previous node results
   - Building final output

Usage:
-----
python two_step.py

Expected Output:
    The number 5 doubled is 10
"""

from typing import TypedDict
from langgraph.graph import StateGraph, END

class CounterState(TypedDict):
    """
    Defines the state structure for number processing workflow.

    Attributes:
        number (int): Input number to process
        doubled (int): Number after doubling
        message (str): Final formatted message
    """
    number: int
    doubled: int
    message: str

def double_number(state: CounterState) -> dict:
    """
    First step: doubles the input number.

    Args:
        state (CounterState): Current state with input number

    Returns:
        dict: Updated state with doubled number

    Example:
        >>> double_number({"number": 5})
        {"doubled": 10}
    """
    doubled = state["number"] * 2
    return {"doubled": doubled}

def create_message(state: CounterState) -> dict:
    """
    Second step: creates a formatted message with the results.

    Args:
        state (CounterState): Current state with original and doubled numbers

    Returns:
        dict: Updated state with formatted message

    Example:
        >>> create_message({"number": 5, "doubled": 10})
        {"message": "The number 5 doubled is 10"}
    """
    return {"message": f"The number {state['number']} doubled is {state['doubled']}"}

# Create graph with our state type
workflow = StateGraph(CounterState)

# Add nodes in sequence
workflow.add_node("doubler", double_number)    # First operation
workflow.add_node("messenger", create_message)  # Second operation

# Define graph flow: start -> doubler -> messenger -> end
workflow.set_entry_point("doubler")            # Start with doubler
workflow.add_edge("doubler", "messenger")      # Connect doubler to messenger
workflow.add_edge("messenger", END)            # End after messenger

# Compile the graph into a runnable app
app = workflow.compile()

if __name__ == "__main__":
    # Run the workflow with a test number
    result = app.invoke({"number": 5})
    print(result["message"])  # Prints: The number 5 doubled is 10
