from tools.memory import retrieve_memory


def memory_agent(state):

    print(
        "Running Memory Agent..."
    )

    topic = state["topic"]

    memory = retrieve_memory(
        topic
    )

    return {
        "memory": memory
    }