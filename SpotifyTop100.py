from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

CLIENT_ID = "YOUR CLIENT ID"
CLIENT_SECRET = "YOUR CLIENT SECRET"

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]
artist_span = soup.select("li ul li span")
artist_names = [artist.getText().strip() for artist in artist_span]
artist_names = artist_names[::7]

manager = SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR USERNAME")

sp = spotipy.Spotify(auth_manager=manager)
user_id = sp.current_user()["id"]

token = manager.get_access_token(as_dict=False)
auth_code = manager.get_authorization_code()

playlist = sp.user_playlist_create(user=user_id, name="Top 100 songs on the day you were born", public=False, description="Top 100 Billboard song on day " + date)
playlist_id = playlist["id"]

track_ids = []
unsuccessful_tracks =[]
unsuccessful_artists = []

for i in range(0, 100):
    track_info = sp.search(q='artist:' + artist_names[i] + ' track:' + song_names[i], type='track')
    try:
        track_id = track_info["tracks"]["items"][0]["id"]
        track_ids.append(track_id)
    except:
        unsuccessful_tracks.append(song_names[i])
        unsuccessful_artists.append(artist_names[i])

# track_info = sp.search(q='artist:' + unsuccessful_artists[0] + ' track:' + unsuccessful_tracks[0], type='track')
# pprint(track_info)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_ids)





