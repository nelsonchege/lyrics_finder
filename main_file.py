import lyrics
from artist_songs import artist_songs
from database import select_data
from play_song import play_music


# initioate the main method for the whole project
def main():
    # select variable is used to navigate through menu which has four options
    selected_option = int(input("menu:"
                                " \n 1. search  \n 2. view saved  \n 3. play song \n"
                                " 4. exit \n"
                                ))
    # select variable is used to navigate through menu
    # which has four options and the user select value higher than four
    while selected_option < 1 or selected_option > 4:
        selected_option = int(input("options between 1 and 3:"
                                    " \n 1. search \n 2. view saved   \n 3. play song \n"
                                    " 4. exit \n"
                                    ))

    if selected_option == 1:
        # if user selects option one it proms into another menu for searching
        selected_option_2 = int(input("what do you want to search:"
                                      " \n 1. song lyrics  \n 2. artist songs  \n 3. back "
                                      " \n 4. exit \n"
                                      ))
        # select variable is used to navigate through menu
        # which has four options and the user select value higher than four
        while selected_option_2 < 1 or selected_option_2 > 4:
            selected_option_2 = int(input("please choose  between 1 and 3:"
                                          " \n 1. song lyrics  \n 2. artist songs  \n 3. back "
                                          " \n 4. \n"
                                          ))
        if selected_option_2 == 1:
            # prompts user
            art = input("please enter artist name:")
            son = input("enter song for lyrics you want:")
            # imported method from lyrics file to get lyrics
            # parameters are the two user input
            lyrics.get_lyrics(art, son)
        if selected_option_2 == 2:
            # imported method from artist_songs file to get lyrics
            # parameters are the two user input
            art = input("please enter artist name:")
            sonn = int(input("number of song you want:"))
            artist_songs(art, sonn)
        if selected_option_2 == 3:
            # this loads the main function restarting the program
            main()
        if selected_option_2 == 4:
            # this ends the program
            exit()
    elif selected_option == 2:
        # this method from database file display data stored in data base
        select_data()
        main()
    elif selected_option == 3:
        # this opens youtube to play a song user inputs
        print("what do you want to listen to:")
        name_of_song = input("name of song:")
        # removes whitespace from the user input
        nameofsong = name_of_song.replace(" ", "")
        # method imported from play_song to play music
        play_music(nameofsong)
    else:
        exit()


# prints welcome message when you first run it
print("welcome to lyrics finder")
print("N/B check spelling for song name")
# calling the  main method to start the program

main()
