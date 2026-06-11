from tools.llm_client import ask_llm

def research_agent(state):

    print("Running Research Agent...")

    sources = state["sources"]

    prompt = f"""
    You are a senior research analyst.

    Analyze the following research sources.

    Extract:

    1. Executive Summary
    2. Key Findings
    3. Important Facts
    4. Statistics
    5. Trends
    6. Challenges
    7. Future Opportunities

    Sources:

    {sources}

    Return detailed research notes.
    """

    research = ask_llm(prompt)

    return {
        "research": research
    }