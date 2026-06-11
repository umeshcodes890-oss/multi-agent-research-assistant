from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_web(query):

    result = client.search(
        query=query,
        max_results=5
    )

    formatted_results = []

    for item in result["results"]:

        formatted_results.append(
            f"""
TITLE: {item.get('title', '')}

CONTENT:
{item.get('content', '')}

SOURCE:
{item.get('url', '')}
"""
        )

    return formatted_results