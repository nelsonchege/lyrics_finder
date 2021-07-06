import lyricsgenius


# initiate function that searches for artist songs
def artist_songs(art, son):
    try:
        token = "y8IsDtp3KNa43X4kTUFadeAkRNAOkaLdCYQ3jex-ivImMSTT4NeNL-6TeJ3Js5Cp"
        # this combine the token given by genius as key
        # then combine us lyricsgenius to access methods in the module
        genius = lyricsgenius.Genius(token)
        # the two parameters which are artist name=art and number of song=son
        # used method .search_artist from lyricsgenius to get all song of the artist
        artist = genius.search_artist(art, max_songs=son, sort="title")
        print(artist.songs)
    except:
        print("no result found")
