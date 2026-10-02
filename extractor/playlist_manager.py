from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path('/Users/urielle.zach/SpotifyAutomation')
folder = PROJECT_ROOT / 'playlistcsv'
output_path = PROJECT_ROOT / 'combined_playlist.csv' 


def get_combined_playlist(output_file=output_path):
    csv_files = sorted(folder.glob("*.csv"))

    if not csv_files:
        print("[Auto-Run] No CSV files found.")
        return None

    unrenamed = [csv for csv in csv_files if not csv.name.startswith("processed_")]

    if unrenamed:
        print(f"[Auto-Run] Found {len(unrenamed)} unrenamed files. Renaming...")
        taken = {csv.name for csv in csv_files}
        next_index = 0
        for csv in unrenamed:
            # skip names that already exist so we never overwrite a processed file
            while f"processed_{next_index}.csv" in taken:
                next_index += 1
            new_name = f"processed_{next_index}.csv"
            csv.rename(csv.with_name(new_name))
            taken.add(new_name)

        csv_files = sorted(folder.glob("*.csv"))

    print(f"[Auto-Run] Processing and merging {len(csv_files)} playlists...")

    combined = pd.concat(
        [pd.read_csv(file).assign(source_playlist=file.stem) for file in csv_files],
        ignore_index=True,
    )

    combined.to_csv(output_file, index=False)
    print(f"[Auto-Run] Saved {len(combined)} rows to {output_file}")

    return output_file