from tools.memory import save_memory
from tools.llm_client import ask_llm
from tools.history import save_history
MAX_REVISIONS = 2


def supervisor_agent(state):

    print(
        "Running Supervisor Agent..."
    )

    critique = state.get(
        "critique",
        ""
    )

    revisions = state.get(
        "revision_count",
        0
    )

    draft_report = state.get(
        "draft_report",
        ""
    )

    if revisions >= MAX_REVISIONS:
        save_history(state["topic"],draft_report)

        save_memory(
            state["topic"],
            draft_report
        )

        return {
            "next_step": "finish",
            "report": draft_report
        }

    prompt = f"""
Critique:

{critique}

Reply ONLY:

revise

or

finish
"""

    decision = ask_llm(
        prompt
    ).lower()

    print(
        "Supervisor:",
        decision
    )

    if "revise" in decision:

        return {
            "next_step": "rewrite",
            "revision_count": revisions + 1
        }
    
    save_history(state["topic"],draft_report)

    save_memory(
        state["topic"],
        draft_report
    )

    return {
        "next_step": "finish",
        "report": draft_report
    }