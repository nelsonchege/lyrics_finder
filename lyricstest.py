# test lyricsgenius api
import lyricsgenius
from lyricsgenius import artist

from artist_songs import artist_songs
from lyrics import get_lyrics


def get_lyrics():
    art = "john legend"
    son = "higher"
    lyric = get_lyrics(art, son)
    assert lyric


def get_songs():
    art = "john legend"
    sonn = 4
    num = artist_songs(art, sonn)
    assert num


def selected_option():
    selected_option = int(input("menu:"
                                " \n 1. search  \n 2. view saved  \n 3. exit \n"
                                ))
    assert selected_option


def menu():
    while selected_option < 1 or selected_option > 3:
        selected_option = 3
    assert selected_option


def song_list():
    art = "john legend"
    list = artist_songs(art)
    assert list



