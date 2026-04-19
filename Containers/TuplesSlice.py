cars = ["bmw", "toyota", "audi", "volvo", "tesla", "gmc", "ford"]

print(type(cars))
print(cars)

# get item at given index
print(cars[3])  # volvo

# get item between start and end index exclusive
print(cars[1:4])  # ['toyota', 'audi', 'volvo']

# get item at last index - 1
print(cars[-1])  # gmc

# get item from last index till given index exclusive
print(cars[-5:-1])  # ['audi', 'volvo', 'tesla', 'gmc']

# get item after every 2 steps
print(cars[1:-1:2])  # ['toyota', 'volvo', 'gmc']

# get items from start till given index exclusive
print(cars[:4])  # ['bmw', 'toyota', 'audi', 'volvo']

# get items from start till end with steps
print(cars[::2])  # ['bmw', 'audi', 'tesla', 'ford']

# get every item in list
print(cars[::])
