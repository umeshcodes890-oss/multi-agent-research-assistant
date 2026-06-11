from tools.llm_client import ask_llm

def writer_agent(state):

    print("Running Writer Agent...")

    topic = state["topic"]

    research = state["research"]

    critique = state.get("critique", "")

    old_report = state.get("draft_report", "")

    if not critique:

        prompt = f"""
        You are a professional research writer.

        Topic:
        {topic}

        Research Notes:
        {research}

        Create a detailed research report.

        Structure:

        # Executive Summary

        # Introduction

        # Key Findings

        # Analysis

        # Challenges

        # Future Scope

        # Conclusion

        Output ONLY the report.
        """

    else:

        prompt = f"""
        You are a senior editor.

        Existing Report:

        {old_report}

        Reviewer Feedback:

        {critique}

        Improve the report.

        IMPORTANT:

        - Do NOT thank the reviewer.
        - Do NOT respond to the reviewer.
        - Do NOT explain changes.
        - Return ONLY the improved report.
        """

    report = ask_llm(prompt)

    return {
        "draft_report": report
    }