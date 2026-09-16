# Task:1  Spotify playlist id print

playlist_ids=[101,102,103,104,105]

print(playlist_ids)
print("*"*50)


# Task 2: Add multiple ids using append and extend

playlist_ids.append(210)
print(playlist_ids)


playlist=[2001,2002,2003]
playlist_ids.extend(playlist)
print(playlist_ids)
print("*"*50)


#Task 3: remove playlist id

removed_id=playlist_ids.pop()
print("Removed Id:",removed_id)
print("Remaining Playlist:",playlist_ids)
print("*"*50)



#Task 5: List and Tuple scenario

# Use a list for Zomato orders because orders can be added or removed.
zomato_orders = ["Pizza", "Burger", "Momos"]

# Use a tuple for IPL team names because the team names are fixed.
ipl_teams = ("CSK", "MI", "RCB", "KKR", "SRH")

print("Zomato orders (list):", zomato_orders)
print("IPL teams (tuple):", ipl_teams)
print("*"*50)


#Task 4: Tuple error

insta_filters=("Clarendon","Juno","Ludwig","Lark")
print(insta_filters)

insta_filters[0]="Gingham"
# TypeError: 'tuple' object does not support item assignment













