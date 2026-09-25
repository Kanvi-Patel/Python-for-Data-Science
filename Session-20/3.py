class Movie:
    def __init__(self,rating):
        self._rating=rating

    def set_rating(self,rating):
        if 0<=rating<=10:
            self._rating=rating
        else:
            print("Invalid rating")

    def get_rating(self):
        return self._rating


m1=Movie(8.5)

print("Rating:",m1.get_rating())

m1.set_rating(9)
print("Updated Rating:",m1.get_rating())

m1.set_rating(15)
