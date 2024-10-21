import requests
from datetime import datetime

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
response = requests.post(url=pixela_endpoint, json=parameters)

# print(response.text)
# url="https://pixe.la/@kmusty"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "commit",
    "type": "int",
    "color": "sora",
}
headers = {
    "X-USER-TOKEN": TOKEN,
}
# graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# posting
today = datetime.now()
date_of = today.strftime("%Y%m%d")
post_endpoint = f"{graph_endpoint}/graph1"
post_parameters = {
    "date": date_of,
    "quantity": "6"
}

post_response = requests.post(url=post_endpoint, json=post_parameters, headers=headers)
print(post_response.text)
