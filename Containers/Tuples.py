# Tuples is similar to array in Java.
# They are immutable. i.e. We can't edit the data in Tuples

user_info = ("Marie", 29, 56.52, "Single", True)

print(type(user_info))  # class tuple
print(user_info)
print(user_info[1])
print(user_info[3])

# unpack the tuples
name, age, weight, married, active = user_info
print(name, age, weight, married, active)

# when we don't know how many items are in the tuples
# first value is assigned to first variable and the remaining are assigned to *other_data
# *other_data is a list of values
name, *other_data = user_info
print(type(name))  # class str
print(type(other_data))  # class list
print(name, other_data)
