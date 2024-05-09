import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import AIMessage, HumanMessage

from helpers import get_city_weather, get_tournament_venue

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4-turbo"

llm = ChatOpenAI(api_key=openai_api_key, model=MODEL)

prompt = hub.pull("hwchase17/openai-tools-agent")

tools = [get_tournament_venue, get_city_weather]

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

conversation_history = []

while (_prompt := input("Enter a prompt (q to quit): ")) != "q":
    conversation_history.append(HumanMessage(content=_prompt))
    result = agent_executor.invoke({"input": _prompt, "chat_history": conversation_history})
    output = result["output"]
    conversation_history.append(AIMessage(content=output))
    print(output)