
from langchain_core.tools import tool
import numexpr


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