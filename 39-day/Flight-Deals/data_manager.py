import requests
from flight_search import FlightSearch


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

    def update_iata(self, sheet):
        flight_search = FlightSearch(api_key="5a9a8861787618bb55e7005540706b98")

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