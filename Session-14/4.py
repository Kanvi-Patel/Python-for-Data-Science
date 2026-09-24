import json

movies=[
    {"title": "3 Idiots", "year": 2009, "rating": 8.4},
    {"title": "Dangal", "year": 2016, "rating": 8.3},
    {"title": "Taare Zameen Par", "year": 2007, "rating": 8.3}
]

with open("movies.json","w") as file:
    json.dump(movies, file,indent=4)

file.close()


file=open("movies.json", "r")

movies=json.load(file)

for movie in movies:
    print(movie["title"], "-", movie["rating"])

file.close()
