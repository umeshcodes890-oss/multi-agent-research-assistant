from tools.llm_client import ask_llm

def critic_agent(state):

    print("Running Critic Agent...")

    report = state["draft_report"]

    prompt = f"""
    You are a research reviewer.

    Review the report.

    Evaluate:

    - Missing information
    - Weak arguments
    - Unsupported claims
    - Clarity
    - Structure

    Report:

    {report}

    Return concise improvement suggestions.
    """

    critique = ask_llm(prompt)

    return {
        "critique": critique
    }