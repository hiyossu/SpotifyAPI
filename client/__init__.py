import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import logging

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

if not client_id or not client_secret:
    raise ValueError("Missing Spotify credentials in environment variables.")

auth_manager = SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope="playlist-read-private" 
)

sp = spotipy.Spotify(
    auth_manager=auth_manager,
    retries = 5,
    status_retries = 5
    )