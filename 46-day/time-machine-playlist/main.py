from bs4 import BeautifulSoup
import requests


travel_year = input("What year you would like to travel to in YYYY-MM-DD format?  ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_year}"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")
songs = []
song_titles = soup.find_all(name="h3", id="title-of-a-story")
for items in song_titles:
    song_in_text = items.get_text(strip=True)
    songs.append(song_in_text)


song_names = songs[6:403:4]
print(len(song_names))
print(song_names)






































#------------------------------- Angela's solution compared to mine---------------------------#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)