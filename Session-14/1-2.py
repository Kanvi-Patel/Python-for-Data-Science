#Task:1

file=open("playlist.txt","w")

file.write("Shape Of You\n")
file.write("Tum Se Hi\n")
file.write("Senorita\n")
file.write("Darkhaast\n")
file.write("Raabta\n")

file.close()

#Task:2

file=open("playlist.txt","r")

for song in file:
    print(song.upper())

file.close()

