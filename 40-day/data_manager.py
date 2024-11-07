import requests
from flight_search import FlightSearch
from main import sheet_data


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_code = {}
        self.api_sheety = ""
        self.headers = {
            "Authorization": ""
        }
        self.customer_data = ""

    def get_data(self):
        response =  requests.get(url=self.api_sheety, headers=self.headers)
        print(response.text)
        self.destination_code = sheet_data["prices"]
        return self.destination_code

    def update_iata(self, sheet):
        flight_search = FlightSearch(api_key="apikey")

        for item in sheet["prices"]:
            if item["iataCode"] == "":
                city_name = item["city"]
                row_id = item["id"]
                put_api = f"{self.api_sheety}/{row_id}"
                iata_code = flight_search.get_iata_code(city_name)
                parameters = {
                    "price": {
                        "iataCode": iata_code
                    }
                }

                put_response = requests.put(url=put_api, json=parameters, headers=self.headers)
                print(put_response.text)
        return sheet

    def get_customer_emails(self):
        customers_endpoint = self.api_sheety
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data