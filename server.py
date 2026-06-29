from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agent import agent
from langchain_core.messages import HumanMessage


app = FastAPI(
    title="AI Agent API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
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


    print("====================")
    print(result)
    print("====================")


    return {
        "response": str(result)
    }