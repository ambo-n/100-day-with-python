import requests,os, pprint
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
SPOTIFY_USER_NAME =os.getenv("SPOTIFY_USER_NAME")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
header = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
url = f"https://www.billboard.com/charts/hot-100/{date}/"
response = requests.get(url=url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text,'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.get_text().strip() for song in song_names_spans] # type: ignore

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
                                  client_secret=SPOTIFY_CLIENT_SECRET,
                                  redirect_uri="http://127.0.0.1:5500/",
                                  scope=scope,
                                  cache_path="token.txt",))

user_id = sp.current_user()["id"] # type: ignore
uri_list = []
year = date.split("-")[0]

for song in song_names:
    result = sp.search(q=f"track:{song}&year:{year}", type="track")
    try:
        uri = result['tracks']['items'][0]['uri'] # type: ignore
        uri_list.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False,description=f"{year} Billboard 100")
playlist_id=playlist['id'] # type: ignore

sp.playlist_add_items(playlist_id=playlist_id,items=uri_list)

