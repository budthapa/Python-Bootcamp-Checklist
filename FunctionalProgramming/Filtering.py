cars = ["Toyota", "Honda", "Ford", "BMW", "Mercedes", "Audi", "Volkswagen", "Nissan", "Hyundai", "Kia"]

# filter the list of cars to include only those that contains letter 'W'
cars_filtered = filter(lambda car: 'W' in car or 'w' in car, cars)  # This will return a filter object of cars that contains letter 'W'
# converting the filter object to a list to see the results
print(list(cars_filtered))  # Output: ['BMW', 'Volkswagen']


# filter the list of cars to include only those that have more than 5 characters
cars_filtered_length = filter(lambda car: len(car) > 5, cars)  # This will return a filter object of cars that have more than 5 characters
# converting the filter object to a list to see the results
print(list(cars_filtered_length))  # Output: ['Toyota', 'Honda', 'Mercedes', 'Volkswagen', 'Nissan', 'Hyundai'] 