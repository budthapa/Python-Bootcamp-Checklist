cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi", "Volkswagen", "Nissan", "Hyundai", "Kia"]
sorted_cars = sorted(cars)  # This will return a new list of cars sorted in alphabetical order
print(sorted_cars)  # Output: ['Audi', 'BMW', 'Ford', 'Honda', 'Hyundai', 'Kia', 'Mercedes', 'Nissan', 'Toyota', 'Volkswagen']      

# reverse sorting
sorted_cars_reverse = sorted(cars, reverse=True)  # This will return a new list of cars sorted in reverse alphabetical order
print(sorted_cars_reverse)  # Output: ['Volkswagen', 'Toyota', 'Nissan', 'Mercedes', 'Kia', 'Hyundai', 'Honda', 'Ford', 'BMW', 'Audi']

# sorting by length of car names
sorted_cars_by_length = sorted(cars, key=len)  # This will return a new list of cars sorted by the length of their names
print(sorted_cars_by_length)  # Output: ['BMW', 'Audi', 'Ford', 'Honda', 'Kia', 'Nissan', 'Toyota', 'Hyundai', 'Mercedes', 'Volkswagen']

two_characters_car = map(lambda s: s[:2], cars)  # This will return a map object of the first two characters of each car name
# the print statement below will consume the map object, and it is empty after this.
print(list(two_characters_car))  # Output: ['To', 'Ho', 'Fo', 'BM', 'Me', 'Au', 'Vo', 'Ni', 'Hy', 'Ki'] 

# or we can simply use the for loop to print the first two characters of each car name without consuming the map object
cars_two_char = [car[:2] for car in cars]

print(sorted(cars_two_char))  # Output: ['Au', 'BM', 'Fo', 'Ho', 'Ki', 'Me', 'Ni', 'To', 'Vo', 'Hy']  