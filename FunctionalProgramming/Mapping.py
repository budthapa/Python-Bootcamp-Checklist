cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi", "Volkswagen", "Nissan", "Hyundai", "Kia"]
# Using map to convert all car names to uppercase
cars_upper = map(str.upper, cars)  # This will return a map object

# converting the map object to a list to see the results
print(list(cars_upper))  # Output: ['TOYOTA', 'HONDA', 'FORD', 'BMW', 'MERCEDES', 'AUDI', 'VOLKSWAGEN', 'NISSAN', 'HYUNDAI', 'KIA']

# using lambda function to get first two letters of each car name
cars_suffix = list(map(lambda sfx: sfx[:2].upper(), cars))  # This will return a list of the first two letters of each car name
print(cars_suffix)  # Output: ['TO', 'HO', 'FO', 'BM', 'ME', 'AU', 'VO', 'NI', 'HY', 'KI']
