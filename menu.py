from lyricsgenius import artist

import lyrics
def menu():
    selected_option = int(input("options:"
                                " \n 1. save \n 2. play  \n 3. exit \n"
                                ))
    while selected_option < 1 or selected_option > 3:
        selected_option = int(input("options between 1 and 3:"
                                    " \n 1. save \n 2. play music  \n 3. exit \n"
                                    ))
    if selected_option == 1:
        artist.save_lyrics()
    elif selected_option == 2:
        print("dababy")
    else:
        exit()