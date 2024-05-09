import os
from openai import OpenAI
from dotenv import load_dotenv

from helpers import tools, get_team_schedule, get_tournament_venue

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

model = "gpt-4-turbo"

def run_bot():
    messages = [
        {"role": "system", "content": "You are a conversational chatbot for a travel agency. Use the available functions to get information if needed. If you do not have enough context or information even from the available function calling, simple reply I do not have enough context"},
        {"role": "user", "content": "What is the venue of the 2028 Olympics tournament?"},
    ]

    bot = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=tools,
        tool_choice="required"
    )
    
    response = bot.choices[0].message

    print(response)

    tool_calls = response.tool_calls

    if tool_calls:

        available_functions = {
            "get_team_schedule": get_team_schedule,
            "get_tournament_venue": get_tournament_venue,
        }

        messages.append(response)

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = eval(tool_call.function.arguments)

            function_response = function_to_call(*function_args.values())

            messages.append({"role": "tool", "name": function_name, "content": function_response, "tool_call_id": tool_call.id})

            new_response = client.chat.completions.create(
                model=model,
                messages=messages,
            )

            return new_response.choices[0].message.content
        
    return response.content

print(run_bot())
