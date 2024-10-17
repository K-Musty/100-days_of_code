# import requests
import json
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

will_rain = False
# weather_data = data["hourly"][0]["weather"][0]["id"]
weather_slice = weather_data = data["hourly"][:3] # For 3 hours
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella ")
print(weather_slice)
