from tools.llm_client import ask_llm

def planner_agent(state):

    print("Running Planner Agent...")

    topic = state["topic"]

    prompt = f"""
    You are a research planner.

    Topic:
    {topic}

    Break this topic into exactly 5 important research areas.

    Return only bullet points.

    Example:

    - History
    - Applications
    - Benefits
    - Challenges
    - Future Trends
    """

    plan = ask_llm(prompt)

    return {
        "plan": plan
    }