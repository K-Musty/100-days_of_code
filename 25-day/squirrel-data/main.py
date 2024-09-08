import pandas
data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")
gray_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "color": ["grey", "red", "black"],
    "count": [gray_squirrel, red_squirrel, black_squirrel]
}
data_fr = pandas.DataFrame(data_dict)
data_fr.to_csv("squirrel_color.csv")
