# main.py
from langgraph.graph import StateGraph
from langgraph.graph import END
from agents.research_agent import fetch_data
from agents.answer_drafter_agent import draft_answer

# Define the state structure
class GraphState(dict):
    pass

# Step 1: Fetch data with the research agent
def run_research(state: GraphState) -> GraphState:
    query = state["query"]
    data = fetch_data(query)
    return {"query": query, "data": data}

# Step 2: Draft the answer using the answer agent
# Step 2: Draft the answer using the answer agent
def run_drafter(state: GraphState) -> GraphState:
    data = state["data"]
    query = state["query"]
    answer = draft_answer(data, query)
    return {"query": query, "data": data, "answer": answer}

# Build the LangGraph
graph = StateGraph(GraphState)
graph.add_node("research", run_research)
graph.add_node("drafter", run_drafter)

graph.set_entry_point("research")
graph.add_edge("research", "drafter")
graph.set_finish_point("drafter")

# Compile and invoke
app = graph.compile()

if __name__ == "__main__":
    query = input("Enter your research query: ")
    result = app.invoke({"query": query})
    print("\n✅ Final Drafted Answer:\n", result["answer"])
