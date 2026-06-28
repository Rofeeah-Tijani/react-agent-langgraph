from agent import agent
from langchain_core.messages import HumanMessage

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content=question
                )
            ]
        }
    )

    print(
        "\nAgent:",
        result["messages"][-1].content
    )