from langchain_core.tools import tool
import requests
import os


@tool
def weather(city: str) -> str:
    """
    Get current weather information for a city.
    """

    api_key = os.getenv("WEATHER_API_KEY")

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={api_key}&units=metric"
    )

    try:
        response = requests.get(
            url,
            timeout=10
        )

        data = response.json()


        # Handle API errors
        if response.status_code != 200:
            return (
                f"Weather service error: "
                f"{data.get('message', 'Unknown error')}"
            )


        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]


        return (
            f"{city}: {description}, {temperature}°C"
        )


    except Exception as e:

        return f"Could not get weather: {e}"