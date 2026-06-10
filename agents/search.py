from tools.web_search import search_web

def search_agent(state):
    print("Running Search Agent...")
    
    plan = state["plan"]

    sources = []

    for topic in plan.split("\n"):
        if topic.strip():
            results = search_web(topic)
            sources.extend(results)

    return {
        "sources": str(sources)
    }