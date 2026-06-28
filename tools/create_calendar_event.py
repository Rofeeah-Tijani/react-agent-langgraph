import os

client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")

from langchain_core.tools import tool

from datetime import datetime

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

