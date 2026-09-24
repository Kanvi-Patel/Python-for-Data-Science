def get_song_duration_per_minute(spotify_playlist):
    try:
        total=0
        for duration in spotify_playlist:
            total=total+duration
        average_duration=total/len(spotify_playlist)
        print("Average duration per song is:",average_duration)
    except ZeroDivisionError as e:
        print("Error Occurred:",e)
    finally:
        print("Calculation completed.")

    
l1=[250,562,125]
get_song_duration_per_minute(l1)

l2=[]
get_song_duration_per_minute(l2)
