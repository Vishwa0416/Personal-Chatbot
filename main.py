# main.py

from dotenv import load_dotenv
from langchain.schema import HumanMessage
from nodes import get_graph
import os

# Load .env
load_dotenv()
chat_graph = get_graph()

# Start chat loop
def main():
    print("🤖 Personal Chatbot (type 'exit' to quit)")
    history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            break

        # Update history and invoke graph
        result = chat_graph.invoke({"history": history + [HumanMessage(content=user_input)]})
        history = result["history"]

        # Print last AI response
        print("Bot:", history[-1].content)

# Access the variable
openai_key = os.getenv("OPENAI_API_KEY")

print("Your OpenAI Key:", openai_key)

if __name__ == "__main__":
    main()
