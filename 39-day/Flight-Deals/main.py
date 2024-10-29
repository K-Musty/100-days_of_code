#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
# from flight_search import FlightSearch


data = DataManager()
# sheet = data.get_data()

sheet_data = {
  "prices": [
    {
      "city": "Paris",
      "iataCode": "",
      "lowestPrice": 54,
      "id": 2
    },
    {
      "city": "Frankfurt",
      "iataCode": "",
      "lowestPrice": 42,
      "id": 3
    },
    {
      "city": "Tokyo",
      "iataCode": "",
      "lowestPrice": 485,
      "id": 4
    },
    {
      "city": "Hong Kong",
      "iataCode": "",
      "lowestPrice": 551,
      "id": 5
    },
    {
      "city": "Istanbul",
      "iataCode": "",
      "lowestPrice": 95,
      "id": 6
    },
    {
      "city": "Kuala Lumpur",
      "iataCode": "",
      "lowestPrice": 414,
      "id": 7
    },
    {
      "city": "New York",
      "iataCode": "",
      "lowestPrice": 240,
      "id": 8
    },
    {
      "city": "San Francisco",
      "iataCode": "",
      "lowestPrice": 260,
      "id": 9
    },
    {
      "city": "Dublin",
      "iataCode": "",
      "lowestPrice": 378,
      "id": 10
    }
  ]
}

# updating sheet
data.update_iata(sheet_data)























#
# def update_iata(sheet):
#     flight_search = FlightSearch()
#     for item in sheet["prices"]:
#       if item["iataCode"] == "":
#         city_name = item["city"]
#         iata_code = flight_search.get_iata_code(city_name)
#         item["iataCode"] = iata_code
#
#     return sheet
#
# data_iata = update_iata(sheet_data)
# print(data_iata)



