from langchain_core.tools import tool
import os
import requests


@tool
def news(topic: str):
    """
    Gets latest news about a topic.

    Use this when the user asks for:
    - latest news
    - current events
    - articles
    - headlines

    Input:
    topic to search for
    """

    try:

        key = os.getenv(
            "NEWS_API_KEY"
        )


        url = (
            "https://newsapi.org/v2/everything"
        )


        params = {
            "q": topic,
            "apiKey": key,
            "language": "en",
            "pageSize": 5
        }


        response = requests.get(
            url,
            params=params
        )


        data = response.json()


        articles = data.get(
            "articles",
            []
        )


        if not articles:
            return "No news found."


        result = ""


        for article in articles:

            result += (
                f"\nTitle: {article['title']}\n"
                f"Description: {article['description']}\n"
                f"URL: {article['url']}\n"
            )


        return result


    except Exception as e:

        return f"News error: {e}"
