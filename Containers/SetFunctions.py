numbers1 = {11, 12, 2, 33, 45, 56, 7, 8, 98, 76}
print(numbers1)

numbers2 = {56, 7, 11, 8, 98, 76, 445, 22, 6664, 765, 234}
print(numbers2)

print(numbers1.union(numbers2))
print(numbers1.intersection(numbers2))
print(numbers2.intersection(numbers1))
print(numbers1.difference(numbers2))  # only the items remaining in numbers1
print(numbers2.difference(numbers1))  # only the items remaining in number2

# only the items found in both numbers1 and numbers2. i.e. remove the intersected numbers
print(numbers1.symmetric_difference(numbers2))
print(numbers2.issuperset(numbers1))

num = numbers1.pop()
print(num)

print(numbers1)