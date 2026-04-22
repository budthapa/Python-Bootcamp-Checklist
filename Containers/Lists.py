# lists are surrounded by square [] brackets
animals = ["cat", "dog", "elephant", "tiger", "lion"]

print(type(animals))
print(id(animals))

animals += ["rhino"]  # add item to list without changing the original list. i.e. append
print(animals)
print(id(animals))

animals[3] = "monkey"  # replace item at given index
print(animals)

# append one item to the list, be it single item or another list
animals.append("fatbear")
animals.append(["puma", "giraffe"])
print(id(animals))
print(animals)
print(len(animals))

# extend the list with items one by one. e.g. the panda below is added as p, a, n, d, a
animals.extend("bigpanda")
animals.extend("monkeybanana")
print(animals)
print(len(animals))

# insert item at specified position
animals.insert(4, "panther")
print(animals)

# convert to tuple
animals_tuple = tuple(animals)
print(animals_tuple)
print(type(animals_tuple))

# convert back to list
animals_list = list(animals_tuple)
print(animals_list)
print(type(animals_list))

# removing items
animals.remove("a")  # removes the first item that it finds
print(animals)

fav_animal = animals.pop(2)  # remove item at the given index and assigned to new variable
print(fav_animal)
print(animals)

print(id(animals))
del animals[3]  # delete item at given index
print(animals)
print(id(animals))  # list is mutable so the id remains the same

animals.clear()  # delete everything in the list
print(animals)
print(id(animals))

