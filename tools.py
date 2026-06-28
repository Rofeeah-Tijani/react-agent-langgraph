from langchain_core.tools import tool
from pathlib import Path
import requests
import sqlite3
from datetime import datetime
import numexpr

# ==========================
# Calculator Tool
# ==========================

@tool
def calculator(expression: str) -> str:
    """
    Performs mathematical calculations.

    Input should be a math expression:
    Example:
    25*4
    100/5
    (10+5)*2
    """

    try:
        result = numexpr.evaluate(expression)

        return str(result)

    except Exception as e:
        return f"Calculation error: {e}"



# ==========================
# File Writer Tool
# ==========================

@tool
def file_writer(filename: str, content: str):
    """
    Creates a file and writes content inside it.
    """

    try:
        path = Path(filename)

        path.write_text(
            content,
            encoding="utf-8"
        )

        return f"{filename} created successfully."

    except Exception as e:
        return f"File error: {e}"



# ==========================
# File Reader Tool
# ==========================

@tool
def file_reader(filename: str):
    """
    Reads content from an existing file.
    """

    try:

        path = Path(filename)

        if not path.exists():
            return "File does not exist."

        return path.read_text(
            encoding="utf-8"
        )

    except Exception as e:
        return f"Read error: {e}"



# ==========================
# Translation Tool
# ==========================

@tool
def translator(text: str, language: str):
    """
    Translates text into another language.

    Example:
    text="Hello"
    language="French"
    """

    return (
        f"Translation requested: "
        f"Translate '{text}' into {language}"
    )



# ==========================
# Weather Tool
# ==========================

@tool
def weather(city: str):
    """
    Gets weather information for a city.

    Uses wttr.in API.
    """

    try:

        response = requests.get(
            f"https://wttr.in/{city}?format=3"
        )

        return response.text


    except Exception as e:
        return f"Weather error: {e}"



# ==========================
# News Tool
# ==========================

@tool
def news(topic: str):
    """
    Searches for news about a topic.

    Demo version.
    """

    return (
        f"News search requested for: {topic}. "
        "Connect a news API for live results."
    )



# ==========================
# Web Search Tool
# ==========================

@tool
def web_search(query: str):
    """
    Searches the web.

    """

    return (
        f"Search results requested for: {query}. "
        "Connect search API here."
    )



# ==========================
# Email Tool
# ==========================

@tool
def send_email(receiver: str, message: str):
    """
    Sends an email.
    """

    return (
        f"Email prepared for {receiver}: {message}"
    )



# ==========================
# Calendar Tool
# ==========================

@tool
def create_calendar_event(
    event: str,
    date: str
):
    """
    Creates a calendar event.
    """

    return (
        f"Calendar event created: {event} "
        f"on {date}"
    )



# ==========================
# PDF Reader Tool
# ==========================

@tool
def read_pdf(filename: str):
    """
    Reads text from a PDF file.
    """

    try:

        from pypdf import PdfReader

        reader = PdfReader(filename)

        text=""

        for page in reader.pages:
            text += page.extract_text()

        return text


    except Exception as e:
        return f"PDF error: {e}"



# ==========================
# Database Query Tool
# ==========================

@tool
def database_query(query: str):
    """
    Executes SQL query.

    Uses SQLite database.
    """

    try:

        conn = sqlite3.connect(
            "database.db"
        )

        cursor = conn.cursor()

        cursor.execute(query)

        result = cursor.fetchall()

        conn.close()

        return str(result)


    except Exception as e:
        return f"Database error: {e}"



# ==========================
# Reminder Tool
# ==========================

@tool
def reminder(task: str, time: str):
    """
    Creates a reminder.
    """

    return (
        f"Reminder created: {task} at {time}"
    )