import sqlite3


def database():
    # creating a database using function from sqlite3
    conn = sqlite3.connect('lyrics_database.db')


def create_table():
    conn = sqlite3.connect('lyrics_database.db')
    c = conn.cursor()
    # creating a  table using function from sqlite3
    conn.execute('''CREATE TABLE SONGLYRICS
         (ID INTEGER PRIMARY KEY   AUTOINCREMENT,
         artist_name     TEXT    NOT NULL,
         artist_song     TEXT    NOT NULL,
         Lyrics          TEXT    NOT NULL
         );''')
    print("Table created successfully")
    c.close()


def insert_data(data):
    conn = sqlite3.connect('lyrics_database.db')
    c = conn.cursor()
    # this takes in data and saves it in the database
    c.execute(
        'INSERT INTO SONGLYRICS (artist_name,artist_song,Lyrics) VALUES (?,?,?)',
        (data[0], data[1], data[2]))
    conn.commit()
    c.close()
    print("data inserted successfully")


def select_data():
    conn = sqlite3.connect('lyrics_database.db')
    # function that prints out the data saved in the database
    cursor = conn.execute("SELECT  artist_name, artist_song, Lyrics from SONGLYRICS")
    for row in cursor:
        print ("artist_name = ", row[0])
        print ("artist_song = ", row[1])
        print("Lyrics = ", row[2], "\n")
    print("Operation done successfully")
    # closes after printing the data
    conn.close()

