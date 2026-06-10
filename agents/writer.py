from tools.llm_client import ask_llm
def writer_agent(state):
    print("Running Writer Agent...")
    topic = state["topic"]

    research = state["research"]

    critique = state.get("critique", "")

    prompt = f"""
    Topic:
    {topic}

    Research:
    {research}

    Critique:
    {critique}

    Write or improve the report.
    """

    report = ask_llm(prompt)

    return {
        "draft_report": report
    }