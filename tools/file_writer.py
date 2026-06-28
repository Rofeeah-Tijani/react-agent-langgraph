from langchain_core.tools import tool
from pathlib import Path

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
