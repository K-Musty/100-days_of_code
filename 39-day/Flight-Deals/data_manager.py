import requests
import pprint


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_sheety = "https://api.sheety.co/a62a53f4c52a9eb4be453ec56a4f4616/flightDeals/prices"
        self.headers = {
            "Authorization": "Bearer kalli07046989916"
        }

    def get_data(self):
        response =  requests.get(url=self.api_sheety, headers=self.headers)
        print(response.text)