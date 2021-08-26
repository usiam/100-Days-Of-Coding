import requests, lxml
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

CLIENT_ID = os.environ.get("ID")
CLIENT_SECRET = os.environ.get("SECRET")
scope = "playlist-modify-private"
time = input("Which year do you want to travel to? Type the date in YYYY-MM-DD formal: ")
year = time.split("-")[0]

def get_songs_list(date):
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}").text
    soup = BeautifulSoup(response, "lxml")
    songs = [name.getText() for name in soup.find_all(name="span", class_="chart-element__information__song")]
    return songs

def get_user_id(auth_user):
    user_id = auth_user.current_user()['id']
    return user_id

def get_song_uris(songs):
    song_uri = []
    for song in songs:
        result = sp.search(q=f"track:{song} year:{year}", type="track")
        try:
            uri = result["tracks"]["items"][0]["uri"]
            song_uri.append(uri)
        except IndexError:
            print(f"{song} doesn't exist in Spotify. Skipped.")
    return song_uri

if __name__ == '__main__':
    songs_list = get_songs_list(date=time)
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, redirect_uri="https://example.com/",
                                                   client_id=CLIENT_ID,
                                                   client_secret=CLIENT_SECRET, cache_path='token.txt', show_dialog=True))
    user_id = get_user_id(auth_user=sp)
    song_uris = get_song_uris(songs=songs_list)
    playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)