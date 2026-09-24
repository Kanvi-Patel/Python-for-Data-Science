l1=["CSK","Mumbai Indians", "RCB", "Kolkata Knight Riders", "Punjab Kings"]

print("Teams which names are greater than 6 characters.")
def ipl_teams(list):
    for i in list:
        if len(i)>6:
            print(i)
        else:
            continue

ipl_teams(l1)
    
