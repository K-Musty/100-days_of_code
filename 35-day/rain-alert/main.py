# import requests
import os

from twilio.rest import Client
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
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It will Rain today, be sure to take an umbrella",
        from_="+18643516254",
        to="+2349037256466"
    )
    print(message.status)
elif not will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is sunny, be sure to take alot of water",
        from_="+18643516254",
        to="+2349037256466"
    )
    print(message.status)
    print(message.sid)
