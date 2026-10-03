from langchain_anthropic import ChatAnthropic
from agent.state import AgentState
from agent.tools import get_stock_data

llm = ChatAnthropic(model="claude-haiku-4-5-20251001", temperature=0)

tools = [get_stock_data]
llm_with_tools = llm.bind_tools(tools)


def financial_agent(state: AgentState):
    messages = state.get("message", [])

    response = llm_with_tools.invoke(messages)

    return {"messages": [response]}
