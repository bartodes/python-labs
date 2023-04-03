import openpyxl

songs_file = openpyxl.load_workbook("songsFromPlaylist.xlsx")
songs_list = songs_file["Sheet1"]

playlist_songs = {} #the amount of songs in a playlist
playlist_listeners = {} #the total of listeners per playlist
artist_listeners = {} #the total of listeners per artist
playlist_forgotten_songs = {} #the songs under 100,000 listeners in a playlist


for songs_row in range(2, songs_list.max_row + 1):
    songs = songs_list.cell(songs_row, 1).value
    listeners = songs_list.cell(songs_row, 2).value
    artist = songs_list.cell(songs_row, 3).value
    playlist = songs_list.cell(songs_row, 4).value

    forgotten_value = 100000

    if playlist in playlist_songs:
        playlist_songs[playlist] += 1
    else:
        playlist_songs[playlist] = 1

    if artist in artist_listeners:
        artist_listeners[artist] += listeners
    else:
        artist_listeners[artist] = listeners

    if playlist in playlist_listeners:
        playlist_listeners[playlist] += listeners
    else:
        playlist_listeners[playlist] = listeners
    
    if listeners <= forgotten_value and playlist in playlist_forgotten_songs:
        playlist_forgotten_songs[playlist] += 1
    elif listeners <= forgotten_value:
        playlist_forgotten_songs[playlist] = 1


def songsPerPlaylist():
    print("The total of songs in a playlist")


def listenersPerPlaylist():
    print("The total of listeners of the songs in a playlist")


def listenersPerArtist():
    print("The total listeners per Artits")


def playlistForgottenSongs():
    print("The songs under 100000 listeners")


def addSheet():
    print("Sheet named 'Results' added!")


def main():
    addSheet()
main()