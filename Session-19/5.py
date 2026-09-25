class Song:
    def __init__(self,title,artist,duration=0):
        self.title=title
        self.artist=artist
        self.duration=duration
        print("Song Title:",self.title)
        print("Artist:",self.artist)
        print("Duration:",self.duration,"Seconds")

s1=Song("Kesariya","Arijit Singh")
s2=Song("Apna Bana Le","Arijit Singh",360)




