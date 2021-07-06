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


def format_data_for_display(example_people_data):
    pass


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def format_data_for_excel(example_people_data):
    pass

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""


def menu():
    while selected_option < 1 or selected_option > 3:
        selected_option = 3
    assert selected_option


def song_list():
    art = "john legend"
    list = artist_songs(art)
    assert list



