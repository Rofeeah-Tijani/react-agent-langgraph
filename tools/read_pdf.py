from langchain_core.tools import tool

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