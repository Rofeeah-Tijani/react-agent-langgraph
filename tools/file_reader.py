from langchain_core.tools import tool
from pathlib import Path

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