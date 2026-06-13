from tools.llm_client import ask_llm


def research_agent(state):

    print(
        "Running Research Agent..."
    )

    memory = state.get(
        "memory",
        ""
    )
    academic_sources = state.get(
    "academic_sources",
    ""
)


    sources = state["sources"]

    prompt = f"""
You are a senior research analyst.

Previous Knowledge:

{memory}

Web Sources:

{sources}

Create detailed research notes.

Include:

1. Executive Summary
2. Key Findings
3. Important Facts
4. Statistics
5. Trends
6. Challenges
7. Future Opportunities

Return detailed notes only.
"""

    research = ask_llm(
        prompt
    )

    return {
        "research": research
    }