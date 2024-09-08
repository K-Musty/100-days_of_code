# with open("weather_data.csv", mode="r") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))

import pandas
data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(type(data["temp"]))
# data_dict = data.to_dict()
# print(data_dict)
# # temperature = data["temp"].tolist()
# # average_temp = sum(temperature) / len(temperature)
# # or
# print(data["temp"].mean())
# print(data["temp"].max())

print(data[data.day == "Tuesday"])
print(data[data.temp == data.temp.max()])

monday = (data[data.day == "Monday"])
monday_temp = int(monday.temp)
temp_in_f = monday_temp * 9/5 + 32
print(temp_in_f)
print(monday.condition)
