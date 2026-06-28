from agent import agent
from langchain_core.messages import HumanMessage


questions = [

    "Calculate 50 * 20",

    "What is the weather in Lagos?",

    "Give me the latest AI news",

    "Translate hello world to Spanish",

    "Create a file called notes.txt with the content: AI is the future",

    "Read the file notes.txt",

    "Set a reminder for me to study tomorrow",

]


for question in questions:

    print("\nUSER:")
    print(question)

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=question
                )
            ]
        },
        config={
            "configurable": {
                "thread_id": "testing"
            }
        }
    )


    print("\nAGENT:")
    print(
        result["messages"][-1].content
    )

    print("-"*60)