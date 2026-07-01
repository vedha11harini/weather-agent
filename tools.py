import requests


def get_weather(city):

    url = f"https://wttr.in/{city}?format=j1"

    try:

        data = requests.get(url).json()

        current = data["current_condition"][0]

        return f"""
City : {city}
Temperature : {current['temp_C']} °C
Humidity : {current['humidity']} %
Condition : {current['weatherDesc'][0]['value']}
"""

    except:

        return "Unable to fetch weather."