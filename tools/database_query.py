from langchain_core.tools import tool

import sqlite3

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
