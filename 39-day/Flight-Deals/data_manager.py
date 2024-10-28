import requests
from tensorflow.tools.pip_package.setup import headers


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.api_sheety = ""
        self.headers = {

        }
        self.response =  requests.get(url=self.api_sheety, headers=self.headers)
