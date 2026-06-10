from tools.llm_client import ask_llm

def research_agent(state):
    print("Running Research Agent...")

    sources = state["sources"]

    prompt = f"""
    Analyze these research sources.

    Extract:

    1. Key findings
    2. Important statistics
    3. Trends
    4. Expert opinions

    Sources:

    {sources}
    """

    research = ask_llm(prompt)

    return {
        "research": research
    }