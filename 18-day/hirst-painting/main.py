import colorgram

colors = colorgram.extract('image.jpg', 20)

color = colors[0]
print(color)
# for _ in range(20):
#     first_color = colors[0]
