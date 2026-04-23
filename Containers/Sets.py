# surround around with {} curley brackets
# it's similar to Sets in Java. we can only add unique items in set
# set doesnot have a fixed order

numbers = {4, 5, 6, 43, 5, 3, 2, 5, 6, 7, 5, 43, 3, 5, 6, 7, 8, 7, 4, 4, 3}  # only unique numbers are added
print(type(numbers))
print(len(numbers))
print(numbers)

for num in numbers:
    print(num)

numbers.add(584)
print(numbers)

numbers.update({9, 0, 4, 54, 25})  # adding from another collection. i.e. sets
print(numbers)

numbers.update([88, 58, 62])  # adding from another list
print(numbers)

numbers.update((101, 112, 123, 134))  # adding from another Tuples
print(numbers)

# we directly provide the number we want to remove because set doesn't have index
# values are stored in random order
numbers.remove(4)
print(numbers)

number_list = [66, 5, 66, 84, 87, 89]
print(type(number_list))

#  we can simply use set() function to covert list to set
new_set = set(number_list)
print(type(new_set))

n1 = {num * 2 for num in numbers}  # multiply the numbers and reassign it to new set
print(n1)
