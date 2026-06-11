from tools.llm_client import ask_llm

MAX_REVISIONS = 2

def supervisor_agent(state):

    print("Running Supervisor Agent...")

    critique = state.get("critique", "")
    revisions = state.get("revision_count", 0)

    draft_report = state.get("draft_report", "")

    if revisions >= MAX_REVISIONS:

        return {
            "next_step": "finish",
            "report": draft_report
        }

    prompt = f"""
    Critique:

    {critique}

    Decide:

    revise

    or

    finish

    Reply with ONE WORD only.
    """

    decision = ask_llm(prompt).strip().lower()

    print("Supervisor Decision:", decision)

    if "revise" in decision:

        return {
            "next_step": "rewrite",
            "revision_count": revisions + 1
        }

    return {
        "next_step": "finish",
        "report": draft_report
    }