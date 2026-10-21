# AI Agent Tutorial

A Python research assistant built with [LangChain](https://www.langchain.com/) and Google's Gemini models. It can search the web, look up information on Wikipedia, and save research results to a local text file. The response is also parsed into a structured Pydantic model.

## Dependencies

The packages listed in [`requirements.txt`](./requirements.txt) include:

- `langchain`, `langchain-classic`, `langchain-community` — agent and tool building blocks
- `langchain-google-genai` — Google Gemini integration
- `langchain-openai`, `langchain-anthropic` — additional provider integrations
- `ddgs`, `wikipedia` — web search and Wikipedia access
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
   python -m pip install -r requirements.txt
   ```

## Configure Google Gemini

The app requires a Google AI API key. Create a `.env` file in the project root and add:

```dotenv
GOOGLE_API_KEY=your_google_api_key
```

Do not commit `.env` or share your API key. The app loads this file locally when it starts.

## Run

From the project root, with your virtual environment activated:

```bash
python main.py
```

Enter a research question when prompted. The assistant prints the structured research response. The `save_tool` can append results to a text file in the current working directory.

## Contributing

This is a learning project. Feel free to open an issue or pull request with improvements, examples, or documentation updates.