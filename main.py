from pathlib import Path
import os

from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from tools import search_tool, wiki_tool, save_tool
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_google_genai import ChatGoogleGenerativeAI

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.environ["GOOGLE_API_KEY"],
)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# --- STEP 1: Define Clean Prompt for the Agent ---
# We removed the formatting instructions here so the agent can use tools without crashing!
agent_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful research assistant. Answer the query and use tools when necessary."),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

tools = [search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(llm=llm, prompt=agent_prompt, tools=tools)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Run Agent
query = input("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})
agent_output = raw_response.get("output", "")

# --- STEP 2: Structure the Agent's output into Pydantic format ---
print("\n--- Formatting Output into Pydantic Schema ---")

structuring_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a data formatting assistant. Turn the provided research text into the requested JSON schema.\n{format_instructions}"),
    ("human", "Research data to structure:\n{research_data}")
]).partial(format_instructions=parser.get_format_instructions())

# A quick, direct LLM call to safely format the text into the ResearchResponse model
structuring_chain = structuring_prompt | llm | parser

try:
    structured_response = structuring_chain.invoke({"research_data": agent_output})
    print("\n[SUCCESSFULLY PARSED RESEARCH OBJECT]:")
    print(structured_response)
except Exception as e:
    print(f"Error parsing structured response: {e}")
    print(f"Raw output was: {agent_output}")