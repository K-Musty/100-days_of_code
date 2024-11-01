#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager


data = DataManager()
sheet = data.get_data()
notification_manager = NotificationManager()
api_key = ""
flight_search = FlightSearch(api_key)

sheet_data = {
  "prices": [
    {
      "city": "Paris",
      "iataCode": "PAR",
      "lowestPrice": 54,
      "id": 2
    },
    {
      "city": "Frankfurt",
      "iataCode": "FRA",
      "lowestPrice": 42,
      "id": 3
    },
    {
      "city": "Tokyo",
      "iataCode": "TYO",
      "lowestPrice": 485,
      "id": 4
    },
    {
      "city": "Hong Kong",
      "iataCode": "HGK",
      "lowestPrice": 551,
      "id": 5
    },
    {
      "city": "Istanbul",
      "iataCode": "STL",
      "lowestPrice": 95,
      "id": 6
    },
    {
      "city": "Kuala Lumpur",
      "iataCode": "KUL",
      "lowestPrice": 414,
      "id": 7
    },
    {
      "city": "New York",
      "iataCode": "NYC",
      "lowestPrice": 240,
      "id": 8
    },
    {
      "city": "San Francisco",
      "iataCode": "SFO",
      "lowestPrice": 260,
      "id": 9
    },
    {
      "city": "Dublin",
      "iataCode": "DUB",
      "lowestPrice": 378,
      "id": 10
    }
  ]
}

# updating sheet
# data.update_iata(sheet_data)
# gett = FlightSearch(api_key)
# res = gett.get_destination_code("London")
# print(res)


def update_iata(sheet):
    for item in sheet["prices"]:
      if item["iataCode"] == "":
        city_name = item["city"]
        iata_code = flight_search.get_iata_code(city_name)
        item["iataCode"] = iata_code

    return sheet
tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet:
    flight = flight_search.get_flight(
        "LON",
        "NGR",
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight.price < destination["lowestPrice"]:
      notification_manager.send_sms(
        message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airpor}"
                f" to {flight.destination_city}-{flight.destination_airport}, "
                f"from {flight.out_date} to {flight.return_date}."
      )
data_iata = update_iata(sheet)
print(data_iata)



