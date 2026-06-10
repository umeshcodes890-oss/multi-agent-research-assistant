from tools.llm_client import ask_llm

def planner_agent(state):
    print("Running Planner Agent...")
    topic = state["topic"]

    prompt = f"""
    Break the following research topic
    into 5 major subtopics.

    Topic:
    {topic}

    Return only bullet points.
    """

    plan = ask_llm(prompt)

    return {
        "plan": plan
    }