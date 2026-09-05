from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path('/Users/urielle.zach/SpotifyAutomation')
folder = PROJECT_ROOT / 'playlistcsv'

def get_combined_playlist():
    csv_files = list(folder.glob("*.csv"))
    
    if not csv_files:
        print("[Auto-Run] No CSV files found.")
        return pd.DataFrame()
        
    if any(not csv.name.startswith("processed_") for csv in csv_files):
        print(f"[Auto-Run] Found {len(csv_files)} unrenamed files. Renaming...")
        for i, csv in enumerate(csv_files):
            new_name = f"processed_{i}.csv"
            new_file_path = csv.with_name(new_name)
            csv.rename(new_file_path)

        csv_files = list(folder.glob("*.csv"))

    print(f"[Auto-Run] Processing and merging {len(csv_files)} playlists...")

    df_list = [
        pd.read_csv(file).assign(source_playlist=file.stem) 
        for file in csv_files
    ]

    return pd.concat(df_list, ignore_index=True)
