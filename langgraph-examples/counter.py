"""
Simple Counter Example using LangGraph
===================================

This example demonstrates a minimal state transformation using LangGraph.
It shows how to create a simple counter that adds 1 to an input number.

Key Concepts:
-----------
1. Simple State Management
   - Basic state structure
   - Minimal state transformation
   - Single node operation

2. Basic Graph Structure
   - One node workflow
   - Direct input/output flow
   - Simple state updates

Usage:
-----
python counter.py

Expected Output:
    Started with 0, count is now 1
"""

from typing import TypedDict
from langgraph.graph import StateGraph, END

class CountState(TypedDict):
    """
    Defines the state structure for the counter.

    Attributes:
        start (int): Initial number
        count (int): Number after adding 1
    """
    start: int
    count: int

def add_one(state: CountState) -> dict:
    """
    Adds 1 to the input number.

    Args:
        state (CountState): Current state with start number

    Returns:
        dict: Updated state with incremented count

    Example:
        >>> add_one({"start": 5})
        {"count": 6}
    """
    return {"count": state["start"] + 1}

# Create graph with our state type
workflow = StateGraph(CountState)

# Add the counter function as a node
workflow.add_node("counter", add_one)

# Define the flow: start -> counter -> end
workflow.set_entry_point("counter")
workflow.add_edge("counter", END)

# Compile the graph into a runnable app
app = workflow.compile()

if __name__ == "__main__":
    # Run the workflow with a starting number
    result = app.invoke({"start": 0})
    print(f"Started with {result['start']}, count is now {result['count']}")

    # Try with a different number
    result = app.invoke({"start": 5})
    print(f"Started with {result['start']}, count is now {result['count']}")
