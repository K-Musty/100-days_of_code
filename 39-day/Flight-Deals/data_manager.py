import requests
from flight_search import FlightSearch


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):


    def get_data(self):
        response =  requests.get(url=self.api_sheety, headers=self.headers)
        print(response.text)

    def update_iata(self, sheet):
        flight_search = FlightSearch()

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