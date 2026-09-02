import pandas as pd
import time
from client import sp

def export_tracks():
    df = pd.read_csv('data/extracted_playlists.csv')
    
    all_tracks = []
    
    print("Starting track export...")
    
    for playlist_id in df['Playlist ID']:
        try:
            print(f"Fetching tracks for playlist: {playlist_id}")
            
            results = sp.playlist_items(playlist_id, limit=100)
            items = results['items']
            
            for item in items:
                track = item.get('track')
                if track:  
                    all_tracks.append({
                        'Playlist ID': playlist_id,
                        'Track Name': track.get('name', 'Unknown'),
                        'Artist': track['artists'][0]['name'] if track.get('artists') else 'Unknown',
                        'Album': track['album']['name'] if 'album' in track else 'Unknown',
                        'Spotify URI': track.get('uri', '')
                    })
            
            time.sleep(0.5) 
            
        except Exception as e:
            print(f"Error fetching tracks for {playlist_id}: {e}")
            
    tracks_df = pd.DataFrame(all_tracks)
    tracks_df.to_csv("data/exported_tracks.csv", index=False)
    
    print(f"\n=== EXPORT COMPLETE ===")
    print(f"Exported {len(all_tracks)} total tracks to data/exported_tracks.csv")