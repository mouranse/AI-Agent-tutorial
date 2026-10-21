# AI Agent Tutorial

A Python learning project for exploring AI agents and language-model integrations with [LangChain](https://www.langchain.com/). The project dependencies include OpenAI and Anthropic integrations, Wikipedia access, environment-variable loading, and data validation.

> **Project status:** This repository is a work in progress. It currently contains the dependency list but does not yet include an application entry point or runnable agent example.

## Dependencies

The packages listed in [`requirments.txt`](./requirments.txt) are:

- `langchain`, `langchain-community` — agent and integration building blocks
- `langchain-openai`, `langchain-anthropic` — OpenAI and Anthropic integrations
- `wikipedia` — Wikipedia access
- `python-dotenv` — loading configuration from a local `.env` file
- `pydantic` — data validation

## Getting started

You will need Python and `pip` installed.

1. Clone the repository and open its directory:

   ```bash
   git clone https://github.com/<your-username>/AI-Agent-tutorial.git
   cd AI-Agent-tutorial
   ```

2. Create and activate a virtual environment.

   **Windows (PowerShell):**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirments.txt
   ```

## Configuration

No API keys are required just to install the dependencies. If you add an example that uses a hosted model, provide the key for the provider you choose through environment variables (for example, `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`). Keep secrets out of source control; use local environment variables or a `.env` file and do not commit credentials.

## Running the project

There is no runnable agent or command-line entry point in the repository yet. Once an example is added, document its run command here.

## Contributing

This is a learning project. Feel free to open an issue or pull request with improvements, examples, or documentation updates.