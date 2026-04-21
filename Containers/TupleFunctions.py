# builtin functions in tuple

# working with numbers
numbers = 1, 2, 3, 6, 0, 9, 4, 5, 8, 7, 2, 1, 5, 4, 9, 6, 8, 5, 4, 8, 2, 1, 0, 3, 2, 0, 1, 5, 4, 8, 5

print(type(numbers))  # tuple
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(numbers.count(8))
print(numbers.index(4))

# working with strings
sentence = "This is an example sentence to work with builtin tuple functions"
print(type(sentence))  # str
print(len(sentence))
print(sentence.count("m"))
print(max(sentence))
print(min(sentence))  # underscore. will print as blank
print(sentence.index("i"))
