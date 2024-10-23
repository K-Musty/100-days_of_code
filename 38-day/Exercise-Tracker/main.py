import requests

parameters = {
    "query": input("Tell me which exercises you did ")
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=api_endpoint, json=parameters, headers=headers)
print(response.text)