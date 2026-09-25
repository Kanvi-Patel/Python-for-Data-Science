#Task:1

class Song:
    def __init__(self,title,artist,duration):
        self.title=title
        self.artist=artist
        self.duration=duration
        print("Song Title:",self.title)
        print("Artist:",self.artist)
        print("Duration:",self.duration,"Seconds")
#Task:2
    def play_preview(self):
            print(f"Playing 30-second preview of {self.title} by {self.artist}")

s1=Song("Kesariya","Arijit Singh",268)
s1.play_preview()



