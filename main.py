from langchain.agents import initialize_agent, AgentType
from langchain_community.llms import Ollama
from tools.file_search_tool import search_file
from tools.find_latest_file_by_extension import find_latest_file_by_extension
from tools.open_tool import open_path

llm = Ollama(model="mistral")

tools = [search_file, find_latest_file_by_extension, open_path]


agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True
)

# 💬 CLI loop
while True:
    user_input = input("\n Ask your agent (or type 'exit'): ")
    if user_input.strip().lower() in {"exit", "quit"}:
        break
    try:
        response = agent.invoke(user_input)
        print("\n Agent response:", response)
    except Exception as e:
        print(f"⚠️ Error: {e}")
