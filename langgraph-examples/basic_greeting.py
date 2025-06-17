from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define what data will flow through our graph
class GreetingState(TypedDict):
    name: str
    message: str

# Define a simple function that creates a greeting
def greet(state: GreetingState):
    return {"message": f"Hello, {state['name']}!"}

# Create the graph
workflow = StateGraph(GreetingState)

# Add the greet function as a node
workflow.add_node("greeter", greet)

# Set where the graph starts
workflow.set_entry_point("greeter")

# Set where the graph ends
workflow.add_edge("greeter", END)

# Compile the graph
app = workflow.compile()

if __name__ == "__main__":
    # Run the graph
    result = app.invoke({"name": "Alice"})
    print(result["message"])  # Prints: Hello, Alice!
