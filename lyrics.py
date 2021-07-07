import lyricsgenius

from database import insert_data
from play_song import play_music


def get_lyrics(art, son):
    token = "y8IsDtp3KNa43X4kTUFadeAkRNAOkaLdCYQ3jex-ivImMSTT4NeNL-6TeJ3Js5Cp"
    genius = lyricsgenius.Genius(token)
    # function that searches for the artist from lyricsgenius
    artist = genius.search_artist(art, max_songs=1, sort="title")
    # used try except if song not found skips try and goes to the except
    try:
        # searches for song by artist
        song = genius.search_song(son, artist.name)
        # saves the lyrics into a variable
        single_lyrics = song.lyrics
        print(song.lyrics)
        print("\n =========================================== \n")
        # displays a menu for the user for what to do next after getting the lyrics
        selected_option = int(input("options:"
                                    " \n 1. save \n 2. play  \n 3. exit \n"
                                    ))
        while selected_option < 1 or selected_option > 3:
            selected_option = int(input("options between 1 and 3:"
                                        " \n 1. save \n 2. play music  \n 3. exit \n"
                                        ))
        if selected_option == 1:
            try:
                data = [art, son, single_lyrics]
                insert_data(data)
            except:
                print("45")
        elif selected_option == 2:
            son1 = son.replace(" ", "")
            play_music(son1)
        else:
            exit()
        response ='successful'
        return response
    except:
        # this execute when no lyrics is found in lyricsgenius database
        print("\n =========================================== \n")
        print("sorry lyrics not found !!!")
        selected_option = int(input(
                                    " \n 1. exit \n"
                                    ))
        while selected_option < 1 or selected_option > 1:
            selected_option = int(input(" only options 1 :"
                                        " \n 1. exit \n"
                                        ))

            exit()
        response = 'failed'
