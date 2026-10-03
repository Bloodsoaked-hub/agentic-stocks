import os
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import HumanMessage
from agent.graph import app


if not os.getenv("ANTHROPIC_API_KEY"):
    raise ValueError("API key is missing!")

def run_test():
    print("Financial Agent Test")

    query = "What is the current stock price and market cap of Apple (AAPL)?"
    print(f"User Query: {query}\n")

    initial_state = {"messages": [HumanMessage(content=query)]}\

    for event in app.stream(initial_state):
        for node_name, state_value in event.items():
            print(f"[{node_name}] executed.")
            latest_message = state_value["messages"][-1]
            print(f"Content: {latest_message.content}\n")

    print("Test Finished")

if __name__ == "__main__":
    run_test()