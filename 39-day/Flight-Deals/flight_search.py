import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):

    def get_iata_code(self, city_name):
        aviation_params = {
            "access_key": self.api_key,
            "search": city_name
        }
        response = requests.get(self.aviation_api, params=aviation_params)
        aviation_data = response.json()
        print(aviation_data)

        if "data" in aviation_data and len(aviation_data["data"]) > 0:
            for entry in aviation_data["data"]:
                print(entry)
                if entry["city"].lower() == city_name.lower() and entry["iata_code"]:
                    return entry["iata_code"]
        return None

    # def get_flight(self):
    #     response = requests.get(url=self.cheap_api, headers=self.headers)
    #     print(response.text)