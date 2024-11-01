class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_code, departure_city, destination_city, destination_code, go_date, return_date):
        self.price = price
        self.departure_code = departure_code
        self.departure_city = departure_city
        self.destination_code = destination_code
        self.destination_city = destination_city
        self.go_date = go_date
        self.return_date = return_date
