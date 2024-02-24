#!/usr/bin/python3

travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Germany", "Hamburg", "Stuttgart"]
},
]

def add_new_country(country_name, visited_times, visited_cities):
    new_country = {}
    new_country["country"] = country_name
    new_country["visits"] = visited_times
    new_country["cities"] = visited_cities
    travel_log.append(new_country)

add_new_country("russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
