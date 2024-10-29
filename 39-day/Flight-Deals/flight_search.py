import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        pass
        # self.cheap_api = "https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip"
        # self.headers = {
        #     "x-rapidapi-key": "fd92ea0d33msh429fef1462a55cdp14a0c9jsnf9852713306a",
        #     "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
        # }

    def get_iata_code(self, city_name):
        # For now, just return "TESTING" for all city names
        return "TESTING"

    # def get_flight(self):
    #     response = requests.get(url=self.cheap_api, headers=self.headers)
    #     print(response.text)