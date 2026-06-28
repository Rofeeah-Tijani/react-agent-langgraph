from langchain_core.tools import tool

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