import pandas as pd 
from client import sp
import time 

def add_to_lib():
    df = pd.read_csv('data/extracted_playlists.csv')
    for playlist_id in df['Playlist ID']:
        try:
            time.sleep(2)
            sp._put(f"playlists/{playlist_id}/followers")
            print(f"added playlist {playlist_id}")
            
        except Exception as e:
            print(f"Error adding {playlist_id}: {e}")

    print("Done! Check your Spotify library.")

def del_from_lib():
    df = pd.read_csv('data/extracted_playlists.csv')
    for playlist_id in df['Playlist ID']:
        try:
            time.sleep(2)
            sp._delete(f"playlists/{playlist_id}/followers")
            print(f"removing playlist {playlist_id}")
            
        except Exception as e:
            print(f"Error deleting {playlist_id}: {e}")

    print("Done! Check your Spotify library.")

