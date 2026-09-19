def get_unique_artists(spotify_playlist1, spotify_playlist2):
    return spotify_playlist1.union(spotify_playlist2)

spotify_playlist1={"Arijit Singh","A.R. Rahman","Taylor Swift"}
spotify_playlist2 = {"Taylor Swift","Ed Sheeran","Arijit Singh"}

unique_artists=get_unique_artists(spotify_playlist1, spotify_playlist2)

print("Unique Artists:",unique_artists)
