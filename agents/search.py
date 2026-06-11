from tools.web_search import search_web

def search_agent(state):

    print("Running Search Agent...")

    topic = state["topic"]
    plan = state["plan"]

    sources = []

    for subtopic in plan.split("\n"):

        if subtopic.strip():

            query = f"{topic} {subtopic}"

            print(f"Searching: {query}")

            results = search_web(query)

            sources.extend(results)
    combined_sources = "\n\n".join(sources)

    return {
        "sources": combined_sources
    }