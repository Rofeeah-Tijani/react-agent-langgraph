from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agent import agent
from langchain_core.messages import HumanMessage, AIMessage


app = FastAPI(
    title="AI Agent API"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


# Request model
class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=request.message
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

    # Extract only the final AI response
    ai_messages = [
        msg for msg in result["messages"]
        if isinstance(msg, AIMessage)
    ]

    final_response = ai_messages[-1].content

    return {
        "response": final_response
    }