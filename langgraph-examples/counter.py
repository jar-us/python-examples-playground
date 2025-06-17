from typing import TypedDict
from langgraph.graph import StateGraph, END

# Define state
class CountState(TypedDict):
    start: int
    count: int

# Add 1 to the number
def add_one(state: CountState):
    return {"count": state["start"] + 1}

# Create graph
workflow = StateGraph(CountState)

# Add node
workflow.add_node("counter", add_one)

# Set flow
workflow.set_entry_point("counter")
workflow.add_edge("counter", END)

# Compile
app = workflow.compile()

if __name__ == "__main__":
    result = app.invoke({"start": 0})
    print(f"Started with {result['start']}, count is now {result['count']}")
