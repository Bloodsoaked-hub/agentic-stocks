from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from agent.state import AgentState
from agent.tools import get_stock_data
from agent.nodes import financial_agent

workflow = StateGraph(AgentState)

workflow.add_node("financial_agent", financial_agent)

tool_node = ToolNode([get_stock_data])
workflow.add_node("tools", tool_node)

workflow.add_edge(START, "financial_agent")

workflow.add_conditional_edges("financial_agent", tools_condition)

workflow.add_edge("tools", "financial_agent")

app = workflow.compile()
