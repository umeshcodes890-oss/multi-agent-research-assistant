from tools.llm_client import ask_llm

def fact_checker_agent(state):
    print("Running Fact Checker Agent...")
    report = state["draft_report"]

    prompt = f"""
    Review this report.

    Identify:

    - Questionable claims
    - Unsupported facts
    - Areas requiring citations

    Report:

    {report}
    """

    fact_check = ask_llm(prompt)

    return {
        "fact_check": fact_check
    }