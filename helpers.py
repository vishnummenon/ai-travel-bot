from langchain.tools import tool

@tool
def get_tournament_venue(tournament) -> str:
    "Get the venue details for a given tournament."
    venue = ""
    if ("2024 kuttim kolum" in tournament.lower()):
        venue = "Kyoto, Japan"
    elif ("olympics" in tournament.lower()):
        venue = "Beijing, China"
    elif ("t20 world cup" in tournament.lower()):
        venue = "New York, USA"
    return venue

@tool
def get_city_weather(city) -> str:
    "Get the current weather for a given city."
    weather = ""
    if (city == "Kyoto"):
        weather = "Sunny"
    elif (city == "Beijing"):
        weather = "Cloudy"
    elif (city == "New York"):
        weather = "Rainy"
    return weather

def get_team_schedule(tournament, team):
    schedule = ["No schedule available for the given team in the given tournament."]
    if ("t20 world cup" in tournament.lower()):
        if ("india" in team.lower()):
            schedule = [
                "Match against Australia on October 15, 2024, at 14:00 in Los Angeles Cricket Stadium.",
                "Match against England on October 18, 2024, at 19:30 in New York Cricket Ground.",
                "Match against South Africa on October 21, 2024, at 16:00 in Chicago Cricket Park.",
                "Match against Pakistan on October 24, 2024, at 13:00 in Miami Cricket Arena.",
                "Match against New Zealand on October 27, 2024, at 18:00 in San Francisco Cricket Stadium.",
            ]

    single_string = " ".join(schedule)
    
    return single_string

tools = [
        {
            "type": "function",
            "function": {
                "name": "get_tournament_venue",
                "description": "Get the venue details for a given tournament.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tournament": {
                            "type": "string",
                            "description": "The name of the tournament, eg. 2024 ICC Men's T20 World Cup",
                        }
                    },
                    "required": ["tournament"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_team_schedule",
                "description": "Get the schedule details for a given team in a tournament.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tournament": {
                            "type": "string",
                            "description": "The name of the tournament, eg. 2024 ICC Men's T20 World Cup",
                        },
                         "team": {
                            "type": "string",
                            "description": "The name of the team, eg. India"
                        }
                    },
                    "required": ["tournament", "team"],
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "get_city_weather",
                "description": "Get the current weather for a given city.",
                "parameters": {
                    "type": "object",
                    "properties": {
                         "city": {
                            "type": "string",
                            "description": "The name of the city, eg. Kyoto"
                        }
                    },
                    "required": ["city"],
                },
            },
        }
    ]