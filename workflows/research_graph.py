from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.planner import planner_agent
from agents.search import search_agent
from agents.research import research_agent
from agents.writer import writer_agent
from agents.critic import critic_agent
from agents.fact_checker import fact_checker_agent
from agents.supervisor import supervisor_agent

def route_after_supervisor(state):

    if state["next_step"] == "rewrite":
        return "writer"

    return END

class ResearchState(TypedDict):
    topic: str

    plan: str
    sources: str
    research: str

    draft_report: str

    critique: str
    fact_check: str

    report: str

    next_step: str
    revision_count: int


graph = StateGraph(ResearchState)

# Add agents
graph.add_node("planner", planner_agent)
graph.add_node("search", search_agent)
graph.add_node("research", research_agent)
graph.add_node("writer", writer_agent)
graph.add_node("critic", critic_agent)
graph.add_node("fact_checker", fact_checker_agent)
graph.add_node("supervisor", supervisor_agent)

# Workflow
graph.set_entry_point("planner")

graph.add_edge("planner", "search")
graph.add_edge("search", "research")
graph.add_edge("research", "writer")
graph.add_edge("writer", "critic")

graph.add_edge("critic", "fact_checker")

graph.add_edge("fact_checker", "supervisor")

graph.add_conditional_edges(
    "supervisor",
    route_after_supervisor,
    {
        "writer": "writer",
        END: END
    }
)

# End workflow
graph.add_edge("supervisor", END)

# Compile
graph = graph.compile()
