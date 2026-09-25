def  playlist_generator(songs):
    for i in songs:
        yield i

songs=["Shape Of You","Tum Se Hi","Senorita"]
playlist=playlist_generator(songs)
print(next(playlist))
print(next(playlist))
print(next(playlist))

