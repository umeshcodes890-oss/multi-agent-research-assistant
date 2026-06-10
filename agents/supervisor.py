from tools.llm_client import ask_llm

MAX_REVISIONS = 2

def supervisor_agent(state):

    critique = state.get("critique", "")
    revisions = state.get("revision_count", 0)
    draft_report = state.get("draft_report", "")

    if revisions >= MAX_REVISIONS:
        return {
            "next_step": "finish",
            "report": draft_report
        }

    prompt = f"""
    Determine whether this report
    needs revision.

    Critique:

    {critique}

    Reply only:

    revise

    or

    finish
    """

    decision = ask_llm(prompt).lower()

    if "revise" in decision:
        return {
            "next_step": "rewrite",
            "revision_count": revisions + 1
        }

    return {
        "next_step": "finish",
        "report": draft_report
    }