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


@app.get("/")
def home():
    return {
        "message": "AI Agent API is running",
        "docs": "/docs"
    }


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


    # Get the final AI response
    answer = messages[-1].content


    return {
        "response": answer
    }