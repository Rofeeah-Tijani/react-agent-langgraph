import os

client_id = os.getenv("GOOGLE_CLIENT_ID")
client_secret = os.getenv("GOOGLE_CLIENT_SECRET")


from langchain_core.tools import tool
@tool
def send_email(receiver: str, message: str):
    """
    Sends an email.
    """

    return (
        f"Email prepared for {receiver}: {message}"
    )
