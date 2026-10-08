import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from agent.graph import app


if not os.getenv("ANTHROPIC_API_KEY"):
    raise ValueError("API key is missing")

def run_chat():
    print("Financial Agent")

    while True:
        print("Type 'quit' to close the chat.\n")        
        user_input = input("You: ")

        if user_input.lower() in ['quit']:
            print("Goodbye")
            break
        if not user_input.strip():
            continue

        initial_state = {"messages": [HumanMessage(content=user_input)]}
        
        for event in app.stream(initial_state):
            for node_name, state_value in event.items():
                latest_message = state_value["messages"][-1]

                if node_name == "tools":
                    print(f"[System] -> Fetched data from Yahoo Finance.")

                elif node_name == "financial_agent" and latest_message.content:
                    if not latest_message.tool_calls:
                        print(f"Agent: {latest_message.content}\n")

if __name__ == "__main__":
    run_chat()