@app.post("/chat")
def chat(message: str):

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=message
                )
            ]
        },
        config={
            "configurable": {
                "thread_id": "user_id"
            }
        }
    )


    messages = result["messages"]


    answer = ""

    for msg in reversed(messages):

        if msg.content:
            answer = msg.content
            break


    return {
        "response": answer
    }