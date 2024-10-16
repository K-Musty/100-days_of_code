import requests
import json
# api_key = "f6f9c5f85cdcd261168cdd9340fdacca"
# parameters =  {
#     "lat": 11.999970,
#     "lon": 8.534860,
#     "appid": api_key,
#     "exclude": "minutely,
# }
# response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
# data = response.json()
with open("weather.json") as file:
    data = json.load(file)
weather_data = data["hourly"][0]["weather"][0]["id"]
print(weather_data)