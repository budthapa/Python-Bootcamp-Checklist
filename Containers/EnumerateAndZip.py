days = {"Sunday", "Monday", "Tuesday", "Wednesday"}
movies = ("Action", "Adventure", "Romance", "Crime", "Comedy")

# enumerate with index and value
for i, day in enumerate(days):
    print(i, day)

# List two collections together, requires at least 2 collections
for day, movie in zip(days, movies):
    print(day, movie)
