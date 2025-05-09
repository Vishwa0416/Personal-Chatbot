import streamlit as st
from langchain.schema import HumanMessage, AIMessage
from main import chat_graph 

st.set_page_config(page_title="Personal Chatbot", layout="centered")
st.title("🤖 Personal Chatbot")

st.markdown("Welcome to your AI-powered personal chatbot! Ask me anything, and I'll do my best to help you.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Say something...")

if user_input:
    st.session_state.chat_history.append(HumanMessage(content=user_input))
    
    result = chat_graph.invoke({"history": st.session_state.chat_history})
    ai_response = result["history"][-1].content

    st.session_state.chat_history.append(AIMessage(content=ai_response))

for msg in st.session_state.chat_history:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").markdown(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").markdown(msg.content)
