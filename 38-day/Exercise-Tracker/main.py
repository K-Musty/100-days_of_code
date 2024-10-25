import requests
from datetime import datetime


exercise_input = input("Tell me which exercises you did ")
parameters = {
    "query": exercise_input,
    "gender": "male",
    "weight_kg": "65",
    "height_cm": "185",
    "age": "22"
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=api_endpoint, json=parameters, headers=headers)
data = response.json()
# print(response.text)

date_today = datetime.now().strftime("%d/%m/%Y")
time_now = datetime.now().strftime("%X")

for exercise in data["exercises"]:
    parameter = {
        "workout": {
            "date": date_today,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    headers = {
        "Authorization": f"Bearer {bearer_token}"
    }

    sheet_response = requests.post(url=sheet_api, json=parameter, headers=headers)
    print(sheet_response.text)
