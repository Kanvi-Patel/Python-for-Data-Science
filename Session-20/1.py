class Playlist():
    def __init__(self,songs):
        self._songs=songs
        print("Song Titles:",self._songs)
    def add_song(self,song):
        self._songs.append(song)

songs=["Kesariya","Apna Bana Le","Darkhaast","Dooron"]
p1=Playlist(songs)
p1.add_song("Tum Se HI")
p1.add_song("Raabta")
p1.add_song("Shaayad")

print("Song Titles:",p1._songs)
