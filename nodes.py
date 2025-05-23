import os
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph
from langchain.schema import HumanMessage, SystemMessage
from typing import TypedDict
from dotenv import load_dotenv

class ChatState(TypedDict):
    history: list

# Initialize OpenAI LLM using environment variable (ensure OPENAI_API_KEY is set)
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(
    openai_api_key=api_key,
    model="gpt-3.5-turbo",
    temperature=0.7
)

def chat_node(state: ChatState) -> ChatState:
    history = state.get("history", [])
    messages = [SystemMessage(content="You are a helpful personal assistant.")] + history
    response = llm(messages)
    return {"history": history + [messages[-1], response]}

def get_graph():
    builder = StateGraph(ChatState)
    builder.add_node("chat", chat_node)
    builder.set_entry_point("chat")
    return builder.compile()
