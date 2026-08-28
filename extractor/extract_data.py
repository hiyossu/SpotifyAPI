import time
from client import sp

keywords = ['sensual', 'intimacy', 'bedroom', 'late night']
all_playlists = []

target_per_keyword = 100 
limit_per_request = 30  

print("Starting bulk extraction...\n")

for keyword in keywords:
    print(f"\n--- Fetching up to {target_per_keyword} playlists for: '{keyword}' ---")
    
    offset = 0
    fetched_count = 0
    
    while fetched_count < target_per_keyword:
        print(f"Requesting offset {offset}...")
        
        results = sp.search(q=keyword, type='playlist', limit=limit_per_request, offset=offset)
        items = results['playlists']['items']
        
        if not items:
            print("No more playlists found for this keyword.")
            break
            
        for item in items:
            if item:
                playlist_name = item['name']
                owner = item['owner']['display_name']
                playlist_id = item['id']
                all_playlists.append(f"[{keyword}] {playlist_name} - ID: {playlist_id}")
                fetched_count += 1
                
                if fetched_count >= target_per_keyword:
                    break
        
        offset += limit_per_request
        time.sleep(2)

print("\n=== EXTRACTION COMPLETE ===")
print(f"Total playlists gathered: {len(all_playlists)}")