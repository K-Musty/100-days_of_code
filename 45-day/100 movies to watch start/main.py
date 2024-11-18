import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL, )

soup = BeautifulSoup(response.text, "html.parser")
movie_list = []
movies = soup.find_all(name="h3", class_="title")
for movie in movies:
    movie_list.append(movie.getText())

# print(movie_list)
reversed_list = movie_list[::-1]
# print(reversed_list)
with open("movies.txt", mode="w") as movies_file:
    for i in reversed_list:
        movies_file.writelines(f"{i}\n")