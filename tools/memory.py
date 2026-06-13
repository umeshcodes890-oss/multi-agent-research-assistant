import chromadb

client = chromadb.PersistentClient(
    path="./memory/chroma_db"
)

collection = client.get_or_create_collection(
    name="research_memory"
)


def save_memory(topic, content):

    try:

        collection.upsert(
            ids=[topic],
            documents=[content],
            metadatas=[
                {
                    "topic": topic
                }
            ]
        )

    except Exception as e:

        print(
            f"Memory Save Error: {e}"
        )


def retrieve_memory(query):

    try:

        results = collection.query(
            query_texts=[query],
            n_results=3
        )

        docs = results["documents"][0]

        return "\n\n".join(docs)

    except Exception as e:

        print(
            f"Memory Retrieval Error: {e}"
        )

        return ""