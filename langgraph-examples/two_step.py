from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define state
class CounterState(TypedDict):
    number: int
    doubled: int
    message: str

# First step: double the number
def double_number(state: CounterState):
    doubled = state["number"] * 2
    return {"doubled": doubled}

# Second step: create message
def create_message(state: CounterState):
    return {"message": f"The number {state['number']} doubled is {state['doubled']}"}

# Create graph
workflow = StateGraph(CounterState)

# Add nodes
workflow.add_node("doubler", double_number)
workflow.add_node("messenger", create_message)

# Set the flow: doubler -> messenger -> end
workflow.set_entry_point("doubler")
workflow.add_edge("doubler", "messenger")
workflow.add_edge("messenger", END)

# Compile
app = workflow.compile()

if __name__ == "__main__":
    result = app.invoke({"number": 5})
    print(result["message"])  # Prints: The number 5 doubled is 10
