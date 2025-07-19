import requests
from flight_data import FlightData
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, api_key):
        self.api_key = api_key
        self.cheap_api = "https://kiwi-com-cheap-flights.p.rapidapi.com/round-trip"
        self.aviation_api = "https://api.aviationstack.com/v1/cities"
        self.headers = {
            "x-rapidapi-key": "fd92ea0d33msh429fef1462a55cdp14a0c9jsnf9852713306a",
            "x-rapidapi-host": "kiwi-com-cheap-flights.p.rapidapi.com"
        }

    def get_iata_code(self, city_name):
        aviation_params = {
            "access_key": self.api_key,
            "search": city_name
        }
        response = requests.get(self.aviation_api, params=aviation_params)
        aviation_data = response.json()
        print(aviation_data)

        if "data" in aviation_data and len(aviation_data["data"]) > 0:
            print(f"No data found for city: {city_name}")
            for entry in aviation_data["data"]:
                print(entry)
                if entry["city"].lower() == city_name.lower() and entry["iata_code"]:
                    return entry["iata_code"]
        return None

    def get_destination_code(self, city_name):
        location_endpoint = self.aviation_api
        params = {
            "access_key": self.api_key,
            "search": city_name
        }
        response = requests.get(url=location_endpoint, params=params)
        results = response.json()["data"]
        print(results)

        # Find the city that matches the requested name and return the IATA code
        for result in results:
            if result["city"] and result["city"].lower() == city_name.lower():
                return result["iata_code"]

        return None
    def get_flight(self, origin_city_code, destination_city_code, from_time, to_time):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        response = requests.get(url=self.cheap_api,params=query, headers=self.headers)
        print(response.text)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            departure_city=data["route"][0]["cityFrom"],
            departure_code=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_code=data["route"][0]["flyTo"],
            go_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data