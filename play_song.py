import urllib.request
import re
import webbrowser


# define function that plays music
# parameter needed is the name of the music
def play_music(music_name):
    # from the module urllib.request has functions
    # functions which help in opening/retrieving urls
    # saving the user input together with youtube url
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + music_name)
    # converts the user input into youtube request formart
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_link = "https://www.youtube.com/watch?v=" + video_ids[0]
    # opens youtube on chrome using webbrowser module
    response='successful'
    return webbrowser.open(video_link),response
