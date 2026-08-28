import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

if not client_id or not client_secret:
    print("Error: Missing credentials.")
    exit()

try:
    auth_manager = SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    )
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # 2. Make a minimal query (search for 1 track)
    result = sp.search(q="Daft Punk", type="track", limit=1)
    track_name = result["tracks"]["items"][0]["name"]
    artist_name = result["tracks"]["items"][0]["artists"][0]["name"]
    
    print("Spotify API Connection Successful!")
    print(f"Sample response: '{track_name}' by {artist_name}")

except spotipy.exceptions.SpotifyException as e:
    print(f"Spotify API Error: {e.http_status} - {e.msg}")
except Exception as e:
    print(f"Unexpected Error: {e}")