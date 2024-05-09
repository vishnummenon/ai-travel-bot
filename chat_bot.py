from openai import OpenAI
import streamlit as st
import os
from dotenv import load_dotenv

from helpers import tools, get_team_schedule, get_tournament_venue

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-4-turbo"

client = OpenAI(api_key=openai_api_key)

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = model

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a conversational chatbot for a travel agency. Use the available functions to get information if needed. If you do not have enough context or information even from the available function calling, simple reply I do not have enough context"},
    ]

for message in st.session_state.messages:
    if message["role"] != "system" and message["role"] != "tool":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("What's up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=st.session_state.messages,
            tools=tools,
        )
        message = stream.choices[0].message
        tool_calls = message.tool_calls

        if tool_calls:
            available_functions = {
                "get_team_schedule": get_team_schedule,
                "get_tournament_venue": get_tournament_venue,
            }

            st.session_state.messages.append({"role": message.role, "tool_calls": tool_calls, "content": str(message.content or '')})

            for tool_call in tool_calls:
                function_name = tool_call.function.name
                function_to_call = available_functions[function_name]
                function_args = eval(tool_call.function.arguments)

                function_response = function_to_call(*function_args.values())

                st.session_state.messages.append({"role": "tool", "name": function_name, "content": function_response, "tool_call_id": tool_call.id})

                new_stream = client.chat.completions.create(
                    model=st.session_state["openai_model"],
                    messages=st.session_state.messages,
                    tools=tools,
                )

                new_answer = new_stream.choices[0].message.content

                st.markdown(new_answer)

                st.session_state.messages.append({"role": "assistant", "content": new_answer})

        else:
            response = st.markdown(message.content)
            st.session_state.messages.append({"role": "assistant", "content": message.content})