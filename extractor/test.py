from client import sp 

def test():
    try:
        result = sp.search(q="Daft Punk", type="track", limit=1)
        track_name = result["tracks"]["items"][0]["name"]
        artist_name = result["tracks"]["items"][0]["artists"][0]["name"]
        
        print("Spotify API Connection Successful!")
        print(f"Sample response: '{track_name}' by {artist_name}")

    except sp.exceptions.SpotifyException as e:
        print(f"Spotify API Error: {e.http_status} - {e.msg}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


test()

