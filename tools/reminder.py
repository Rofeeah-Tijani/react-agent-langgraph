from langchain_core.tools import tool

from datetime import datetime

@tool
def reminder(task: str, time: str):
    """
    Creates a reminder.
    """

    return (
        f"Reminder created: {task} at {time}"
    )