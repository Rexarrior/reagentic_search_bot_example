# Reagentic Search Example

This example demonstrates how to build a web search agent using the Reagentic framework.

## Overview

The agent is designed to answer questions using only information from the web. It uses a `web_search_t` tool to find information and is explicitly instructed not to rely on its own knowledge. A key feature of this agent is its instruction to consult at least five sources before providing an answer, ensuring more comprehensive and reliable results.

This example can be run interactively in the terminal, in a debug mode with predefined queries, or as a Telegram bot.

## Features

- **Web Search**: The agent can search the web to answer user queries.
- **Multi-Source Verification**: The agent is instructed to consult at least 5 sources before answering.
- **Strict Sourcing**: The agent is instructed to only use information from search results and to cite its sources.
- **Multiple Run Modes**:
    - Interactive command-line chat
    - Debug mode with predefined queries
    - Telegram Bot Integration

## How to Run

### 1. Set Up Your Environment

First, install the required dependencies:

```bash
pip install -r search_example/requirements.txt
```

Next, you need to set up your environment variables. Create a `.env` file in the project root or export them in your shell:

```
# Required for the agent's model provider
OPENROUTER_API_KEY="your_openrouter_api_key"

# Required for the Telegram bot
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
```

### 2. Run the Agent

You can run the agent in three modes:

- **Interactive Mode**: Chat with the agent directly in your terminal.
  ```bash
  python -m search_example.run
  ```

- **Debug Mode**: Run a series of predefined queries to test the agent's functionality.
  ```bash
  python -m search_example.debug
  ```

- **Telegram Bot**: Run the agent as a Telegram bot.
  ```bash
  python -m search_example.telegram_bot
  ```

## Code Structure

- `search_example/`: The main package directory.
  - `agent.py`: Defines the search agent, its instructions, and tool connections.
  - `run.py`: Contains the logic for running the agent in interactive mode.
  - `debug.py`: Contains the logic for running the agent in debug mode.
  - `telegram_bot.py`: Runs the agent as a Telegram bot.
  - `search_subsystem.py`: Defines the `web_search_t` tool for performing web searches.
  - `requirements.txt`: Python dependencies.
  - `.gitignore`: Specifies files to be ignored by version control.