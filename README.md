# Agentic Financial Assistant

A terminal-based, autonomous AI agent for financial analysis, built with LangGraph and Anthropic Claude. The agent processes natural language queries, dynamically decides when to fetch real-time market data, and maintains conversation context to provide accurate financial insights.

## Tech Stack

- **Python 3** — core language
- **LangGraph** — stateful, multi-actor application framework for building agentic workflows
- **LangChain** — LLM integration utilities
- **Anthropic API (Claude Haiku)** — core reasoning engine and structured tool calling
- **yfinance** — real-time market data and stock information retrieval
- **python-dotenv** — environment variable management

## Architecture

The project follows a modular agentic architecture to keep responsibilities separated and make the workflow highly extensible:

```text
User Input → State → Agent Node (Claude) ↔ Tool Node (yfinance) → Output
```

- **State** (`agent/state.py`) — defines the `AgentState` (a `TypedDict` with a message history reducer). It acts as the shared memory that travels through the graph.
- **Tools** (`agent/tools.py`) — defines the external capabilities of the agent using the `@tool` decorator. Contains the exact schemas Claude uses to format its function calls.
- **Nodes** (`agent/nodes.py`) — contains the business logic for the LLM. Initializes the Claude model, binds the tools to it, and processes the current state.
- **Graph** (`agent/graph.py`) — defines the control flow (`StateGraph`). It sets up the edges, conditional routing (checking if the LLM decided to call a tool), and compiles the final application.
- **Main** (`main.py`) — the entry point that initializes the interactive CLI chat loop and streams the graph's output.

The workflow uses a dynamic feedback loop. The LLM is invoked and can either return a final conversational response or a tool invocation request. If a tool is requested, the workflow routes to the Tool Node, executes the external API call, and routes the raw data back to the LLM to formulate a natural language response.

## Project Structure

```text
agentic-stocks/
├── agent/
│   ├── __init__.py
│   ├── state.py           # Agent memory and data structure
│   ├── tools.py           # yfinance API integration and tool definitions
│   ├── nodes.py           # Claude initialization and tool binding
│   └── graph.py           # StateGraph workflow routing and compilation
├── .env                   # Environment variables (git-ignored)
├── .gitignore
├── requirements.txt       # Project dependencies
└── main.py                # App entrypoint and CLI chat loop
```

## Features

- **Interactive CLI Chat** — a continuous conversation loop where users can ask multiple financial questions naturally without restarting the script.
- **Stateful Memory** — built-in conversation history. The agent remembers previous queries in the same session (e.g., asking "What about its market cap?" after asking for Apple's stock price).
- **Dynamic Tool Calling (Agentic RAG)** — Claude automatically parses user intent and decides whether to answer from its internal knowledge or execute a live tool call.
- **Real-Time Financial Data** — integrates `yfinance` to retrieve live stock prices, market caps, sectors, and business summaries directly from Yahoo Finance.
- **Clean Execution Logs** — internal tool-calling thoughts are hidden from the user interface to provide a seamless, human-like chat experience.

## Getting Started

### Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com) (for the reasoning engine)

### Environment Variables

Create a `.env` file in the project root:

```env
ANTHROPIC_API_KEY=your-anthropic-api-key-here
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Bloodsoaked-hub/agentic-stocks.git
cd agentic-stocks
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage Flow

Run the main script to start the interactive chat:

```bash
python main.py
```

1. The terminal will display `You: `.
2. Type a natural language query, even with typos or implicit tickers (e.g., "what is the stock price of tesla").
3. If the agent decides to fetch live data, a `[System] -> Fetched data from Yahoo Finance.` log will appear.
4. The agent will return a formatted, easy-to-read response.
5. Type `quit` to gracefully exit the application.