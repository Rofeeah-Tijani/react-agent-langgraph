
import requests
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("WEATHER_API_KEY")

url = (
    "https://api.openweathermap.org/data/2.5/weather"
    f"?q=Lagos&appid={key}&units=metric"
)

response = requests.get(url)

print(response.status_code)
print(response.json())