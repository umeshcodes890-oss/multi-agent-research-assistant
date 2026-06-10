from tools.llm_client import ask_llm

def critic_agent(state):
    print("Running Critic Agent...")
    report = state["draft_report"]

    prompt = f"""
    Review this report.

    Evaluate:

    - Missing information
    - Weak arguments
    - Unsupported claims
    - Bias
    - Clarity

    Report:

    {report}

    Return improvement suggestions.
    """

    critique = ask_llm(prompt)

    return {
        "critique": critique
    }