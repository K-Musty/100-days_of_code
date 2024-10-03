import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json() # ["iss_position"]["latitude"]
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

iss_position = (longitude, latitude)
print(iss_position)