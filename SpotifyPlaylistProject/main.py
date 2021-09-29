import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Getting the date the user wants to travel to
date = input( "What year you would like to travel to? Enter the date in the YYYY-MM-DD format:  ")
year = date.split("-")[0]

# ---------------------------GETTING DATA FROM BILLBOARD--------------------------

# Billboard url
url = f"https://www.billboard.com/charts/hot-100/{date}"

# Getting the top 100 songs from that date
response = requests.get(url)
contents = response.text

soup = BeautifulSoup(contents, "html.parser")

# Getting the list of the top 100 songs on that date
top_songs_tags = soup.find_all(name = "span",
                               class_ = "chart-element__information__song")
top_songs = [tag.string for tag in top_songs_tags]


# ----------------------MAKING PLAYLIST AND ADDING SONGS TO SPOTIFY-----------------

Spotify_client_ID = ######
Spotify_client_secret = ######

# Authenticating user and getting token
token = spotipy.util.prompt_for_user_token(id,
                                           scope="playlist-modify-public",
                                           client_id=Spotify_client_ID,
                                           client_secret=Spotify_client_secret,
                                           redirect_uri="http://example.com")
sp = spotipy.Spotify(auth = token)

# Getting user id
user_info = sp.current_user()
id = user_info['id']

uri_list = []   # URIs of all 100 songs

# Creating a playlist
playlist = sp.user_playlist_create(user = id,
                                   name = f"{date} Billboard 100",
                                   description = f"Contains the Billboard's top 100 songs on {date}")

songs_skipped = 0
years_to_search = f"{int(year) - 1}-{year}"

# Getting URIs for all the songs. URI- The resource identifier entered in the Spotify'S search box to locate an artist, album, or track.
# Exception handling in the case when the track is not found. In that case output wuld be an empty string.
# Searching songs by name and year
for song in top_songs:
    result = sp.search(
        q=f"track: {song} year: {years_to_search}", type = "track")

    try:
        uri = result['tracks']['items'][0]['uri']
    except IndexError:
        print(f"{song} doesn't exist in spotify. Skipped")
        songs_skipped += 1
    else:
        uri_list.append(uri)

# Adding tracks to playlist
sp.user_playlist_add_tracks(
    user = id, playlist_id = playlist['id'], tracks = uri_list)

print(f"done! skipped: {songs_skipped}")
