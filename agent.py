# agent.py


# 1. Imports

from typing import TypedDict, Annotated 
from langgraph.graph.message import add_messages

from dotenv import load_dotenv

from langgraph.checkpoint.memory import MemorySaver 

memory = MemorySaver()

from langchain_groq import ChatGroq
from langchain_core.messages import (
    HumanMessage,
    SystemMessage
)

from langgraph.graph import (
    StateGraph,
    END
)

from langgraph.prebuilt import (
    ToolNode,
    tools_condition
)


from tools import (
    calculator,
    file_writer,
    file_reader,
    translator,
    weather,
    news,
    web_search,
    send_email,
    create_calendar_event,
    read_pdf,
    database_query,
    reminder
)


# Load environment variables
load_dotenv()



# ==========================
# Initialize LLM
# ==========================
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# ==========================
# Register tools
# ==========================

tools = [
    calculator,
    file_writer,
    file_reader,
    translator,
    weather,
    news,
    web_search,
    send_email,
    create_calendar_event,
    read_pdf,
    database_query,
    reminder
]



# Give tools to the LLM
llm_with_tools = llm.bind_tools(
    tools,
    tool_choice="auto"
)



# ==========================
# Agent State
# ==========================

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]



# ==========================
# LLM Node
# ==========================

def chatbot(state: AgentState):

    system_message = SystemMessage(
    content="""
You are an AI assistant with access to tools.

Use tools whenever needed.

After receiving a tool result, always include the actual result
in your final response.

Do not say only "the result is ready".
"""
)


    response = llm_with_tools.invoke(
        [
            system_message
        ]
        +
        state["messages"]
    )


    return {
        "messages": [
            response
        ]
    }


# ==========================
# Tool Node
# ==========================

real_tool_node = ToolNode(tools)


def tool_runner(state):
    print("\n==========")
    print("TOOL NODE STARTED")
    print(state)
    print("==========\n")

    result = real_tool_node.invoke(state)

    print("\n==========")
    print("TOOL NODE FINISHED")
    print(result)
    print("==========\n")

    return result


tool_node = tool_runner



# ==========================
# Build LangGraph
# ==========================

# ==========================
# Build LangGraph
# ==========================

graph = StateGraph(AgentState)


# Add nodes

graph.add_node(
    "agent",
    chatbot
)


graph.add_node(
    "tools",
    ToolNode(tools)
)


# Start with agent

graph.set_entry_point(
    "agent"
)


# If LLM requests tool -> tools
# Otherwise -> finish

graph.add_conditional_edges(
    "agent",
    tools_condition,
    {
        "tools": "tools",
        END: END
    }
)


# After tool runs, return result to agent

graph.add_edge(
    "tools",
    "agent"
)


# Compile

agent = graph.compile(
    checkpointer=memory
)