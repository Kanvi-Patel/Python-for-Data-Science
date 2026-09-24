from pathlib import Path
import json

file=Path("my_fav_apps.json")

if not file.exists():
    apps=[
        {"name": "Instagram", "category": "Social Media"},
        {"name": "Spotify", "category": "Music"},
        {"name": "Zomato", "category": "Food Delivery"}
    ]
  
    with open(file, "w") as file:
        json.dump(apps, file, indent=4)

    print("File created.")
else:
    print("File already exists.")
