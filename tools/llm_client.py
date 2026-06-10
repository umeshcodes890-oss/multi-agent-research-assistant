import ollama

MODEL_NAME = "gemma3:4b"

def ask_llm(prompt):

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        print(f"LLM Error: {e}")
        return "Error generating response."