from logging import raiseExceptions
from pprint import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope="playlist-modify-private",
                                               cache_path="../token.txt",
                                               show_dialog=True))
USER_ID = sp.current_user()["id"]
PLAYLIST_NAME = "Time Machine Playlist"
PLAYLIST_DESCRIPTION = "Takes top 100 music from date in past"
new_playlist = sp.user_playlist_create(
    user=USER_ID,
    name=PLAYLIST_NAME,
    public=False,
    description=PLAYLIST_DESCRIPTION
)

print(f"Playlist '{PLAYLIST_NAME}' created successfully! Playlist ID: {new_playlist['id']}")


travel_year = input("What year you would like to travel to in YYYY-MM-DD format?  ")

URL = f"https://www.billboard.com/charts/hot-100/{travel_year}"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

song_titles = soup.find_all(name="h3", id="title-of-a-story")

songs = [items.get_text(strip=True) for items in song_titles]

song_names = songs[6:403:4]
# print(len(song_names))
# print(song_names)

songs_uris = []

for song_name in song_names:
    query = f"track: {song_name} year: {year}"
    try:
        new_playlist = sp.search(q=query, type="track")
        songs_uris.append(new_playlist['tracks']['items'][0]['uri'])
    except IndexError:
        print(f"{song_name} does not exist")

pprint(songs_uris)

USER_ID = sp.current_user()["id"]
PLAYLIST_NAME = f"{year} Billboard 100"
PLAYLIST_DESCRIPTION = "Takes top 100 music from date in past"
new_playlist = sp.user_playlist_create(
    user=USER_ID,
    name=PLAYLIST_NAME,
    public=False,
    description=PLAYLIST_DESCRIPTION
)

print(f"Playlist '{PLAYLIST_NAME}' created successfully! Playlist ID: {new_playlist['id']}")
print(new_playlist)

sp.playlist_add_items(playlist_id=new_playlist["id"], items=songs_uris)
print("successful!!!")

























#------------------------------- Angela's solution compared to mine---------------------------#
# soup = BeautifulSoup(response.text, 'html.parser')
# song_names_spans = soup.select("li ul li h3")
# song_names = [song.getText().strip() for song in song_names_spans]
# print(song_names)