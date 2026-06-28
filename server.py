from fastapi import FastAPI
from agent import agent
from langchain_core.messages import HumanMessage


app = FastAPI(
    title="AI Agent API"
)


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


    last_message = result["messages"][-1]


    return {
        "response": last_message.content,
        "message_type": str(type(last_message))
    }