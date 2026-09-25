def print_playlist_songs(songs):
    if len(songs)==0:
        return
    else:
        print(songs[0])
        print_playlist_songs(songs[1:])


songs=["Shape Of You","Tum Se Hi","Senorita"]

print_playlist_songs(songs)
