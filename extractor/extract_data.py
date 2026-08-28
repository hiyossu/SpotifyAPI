from client import sp

keywords = ['workout', 'sensual', 'intimacy', 'bedroom', 'late night']
all_playlists = []

print("Starting extraction...\n")

for keyword in keywords:
    print(f"Fetching playlists for keyword: '{keyword}'...")
    results = sp.search(q=keyword, type='playlist', limit=5) 
    
    for item in results['playlists']['items']:
        if item:
            playlist_name = item['name']
            owner = item['owner']['display_name']
            playlist_id = item['id']
            
            all_playlists.append(f"{playlist_name} (Created by {owner}) - ID: {playlist_id}")

print("\n--- Combined Contextual Results ---")
for idx, playlist in enumerate(all_playlists):
    print(f"{idx + 1}. {playlist}")

