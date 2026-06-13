from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.academic_agent import academic_agent
from agents.planner import planner_agent
from agents.memory_agent import memory_agent
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

    memory: str

    sources: str

    research: str

    draft_report: str

    critique: str

    fact_check: str

    report: str

    next_step: str

    revision_count: int

    academic_sources: str


graph = StateGraph(ResearchState)

# Agents

graph.add_node("planner", planner_agent)

graph.add_node("memory", memory_agent)

graph.add_node("search", search_agent)

graph.add_node("research", research_agent)

graph.add_node("writer", writer_agent)

graph.add_node("critic", critic_agent)

graph.add_node("fact_checker", fact_checker_agent)

graph.add_node("supervisor", supervisor_agent)

graph.add_node(
    "academic",
    academic_agent
)

# Entry

graph.set_entry_point("planner")

# Workflow

graph.add_edge("planner", "memory")

graph.add_edge("memory", "search")

graph.add_edge(
    "search",
    "academic"
)

graph.add_edge(
    "academic",
    "research"
)

graph.add_edge("research", "writer")

graph.add_edge("writer", "critic")

graph.add_edge("critic", "fact_checker")

graph.add_edge("fact_checker", "supervisor")

# Revision Loop

graph.add_conditional_edges(
    "supervisor",
    route_after_supervisor,
    {
        "writer": "writer",
        END: END
    }
)

# Compile

graph = graph.compile()