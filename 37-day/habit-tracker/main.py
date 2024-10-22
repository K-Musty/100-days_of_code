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
# ----------------------------------------------- posting ------------------------------------#
today = datetime.now()
date_of = today.strftime("%Y%m%d")
post_endpoint = f"{graph_endpoint}/graph1"
post_parameters = {
    "date": date_of,
    "quantity": input('How many times did you code today?  ')
}
#
post_response = requests.post(url=post_endpoint, json=post_parameters, headers=headers)
print(post_response.text)
# -------------------------Updating Pixel using PUT request-----------------------------------------------------#

update_endpoint = f"{post_endpoint}/{date_of}"
update_parameters = {
    "quantity": "9"
}

# update_response = requests.put(url=update_endpoint, json=update_parameters, headers=headers)
# print(update_response.text)

# --------------------------------------Deleting a pixel using DELETE request ---------------------------------------------------------------#
delete_endpoint = f"{post_endpoint}/{date_of}"

# delete_response = (requests.delete(url=delete_endpoint, headers=headers))
# print(delete_response.text)
