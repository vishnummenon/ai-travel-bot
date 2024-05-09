import os
from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai.chat_models import ChatOpenAI
import streamlit as st

from helpers import get_city_weather, get_tournament_venue

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4-turbo"

llm = ChatOpenAI(api_key=openai_api_key, model=MODEL)

prompt = hub.pull("hwchase17/openai-tools-agent")

tools = [get_tournament_venue, get_city_weather]

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": """You are a conversational chatbot for a travel agency. Use the available functions to get information if needed. 
         If you do not have enough context or information even from the available function calling, simple reply I do not have enough context
         You can answer any travel or visa related user queries. 
         If the user asks queries on any topic other than travel or visa, you can reply with I am not trained to answer that. """},
        {"role": "assistant", "content": "Hello! How can I help you today?"}
    ]

for message in st.session_state.messages:
    if message["role"] != "system" and message["role"] != "tool":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if _prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": _prompt})
    with st.chat_message("user"):
        st.markdown(_prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            result = agent_executor.invoke({
                "input": _prompt,
                "chat_history": st.session_state.messages,
            })
            output = result["output"]
            st.session_state.messages.append({"role": "assistant", "content": output})
            st.markdown(output)