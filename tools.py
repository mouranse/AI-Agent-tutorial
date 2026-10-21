from datetime import datetime
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool

# --- Safe Wikipedia Integration ---
# Using the stable, native wrapper that doesn't use the buggy 'wikipedia' library
wiki_api = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)

@tool
def wiki_tool(query: str) -> str:
    """Search Wikipedia for encyclopedic facts and historical information."""
    try:
        return wiki_api.run(query)
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}. Use search_tool instead."

# --- DuckDuckGo Web Search Integration ---
search = DuckDuckGoSearchRun()

@tool
def search_tool(query: str) -> str:
    """Search the web for up-to-date information, news, and current events."""
    return search.run(query)

# --- Save to File Integration ---
@tool
def save_tool(data: str, filename: str = "research_output.txt") -> str:
    """
    Saves text data to a specified text file.
    Always provide both 'data' (the content to save) and 'filename' (e.g., 'egypt_research.txt').
    """
    if not filename or filename == "None":
        filename = "research_output.txt"

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"