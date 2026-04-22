# loop through the numbers, calculate and reassign
# this will loop through 0 till 10 and add the number 2 to the list
# we can do this because list are mutable. We can't do this with tuple
numbers = [num + 2 for num in range(0, 11)]
print(numbers)

cars = ["bmw", "ford", "toyota", "tesla", "audi", "gmc", "nissan"]
car_length = [len(car) for car in cars]
print(car_length)

#
large_car = [car for car in cars if len(car) > 3]
print(large_car)

#  make car to upper if length is greater than 3
large_car = [car.upper() if len(car) > 3 else car for car in cars]
print(large_car)
