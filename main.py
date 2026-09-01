from client import sp
from extractor.get_songs import search
from extractor.add_to_lib import add_to_lib
from extractor.test import test


def run_pipeline():
    test()
    search()
    add_to_lib()


if __name__ == '__main__':
    run_pipeline()