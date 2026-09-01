from pathlib import Path
import pandas as pd

folder = Path('/Users/urielle.zach/SpotifyAutomation/playlistcsv')
csv_files = list(folder.glob("*.csv"))

def process_playlist():
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

    global combined_df
    combined_df = pd.concat(df_list, ignore_index=True)

    print(f"[Auto-Run] Complete! Loaded {len(combined_df)} rows into 'combined_df'.")
