# This function takes a variable number of arguments using *args.
# The first argument is treated as a regular parameter, while the rest are collected into a tuple.
def car_names(names, *args):
    print("Car names:", names)
    print("Additional arguments:", args)    
    print("Value at index 1 of additional arguments:", args[1])
    print("Number of additional arguments:", len(args))

car_names("Toyota", "Honda", "Ford", "BMW")

# This function takes a variable number of arguments using *args.
# The first argument is treated as a regular parameter, while the rest are collected into a tuple
def movie_names(favorite_movie, *args):
    print("Favorite movie:", favorite_movie)
    print("Other movie names:", args)
    print("Value at index 0 of movie names:", args[0])
    print("Number of movie names:", len(args))

movie_names("Inception", ["The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"])

# This function takes a variable number of keyword arguments using **kwargs.
# kwargs, also known as keyword arguments, allows you to pass a variable number of named arguments to a function.
# The first argument is treated as a regular parameter, while the rest are collected into a dictionary
def movie_info(title, **kwargs):
    print("Movie title:", title)
    print("Additional info:", kwargs)
    print("Value at key 'director' of additional info:", kwargs.get('director'))
    print("Number of additional info items:", len(kwargs))

movie_info("Inception", director="Christopher Nolan", year=2010, genre="Sci-Fi")