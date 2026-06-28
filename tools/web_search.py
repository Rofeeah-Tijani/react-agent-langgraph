from langchain_core.tools import tool

import requests

from tavily import TavilyClient
import os


client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


@tool
def web_search(query: str):
    """
    Searches the web for current information.
    """

    results = client.search(
        query=query
    )

    return results

