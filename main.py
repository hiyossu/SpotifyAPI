from client import sp
from extractor.search_songs import search
from extractor.add_to_lib import add_to_lib, del_from_lib
from extractor.test import test
from extractor.playlist_manager import process_playlist
from extractor.export import export_tracks

def run_pipeline():
    test()
    search()
    add_to_lib()
    export_tracks()
    process_playlist

    

if __name__ == '__main__':
    run_pipeline()