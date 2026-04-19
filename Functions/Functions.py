# This function calculates the sum of two numbers, 
# with the second number being optional (default is 0).
from distro import name


def calc_sum(num1, num2=0):
    return num1 + num2

num1 = int(input("Enter the first number: ").strip())
num2 = int(input("Enter the second number: ").strip())

result = calc_sum(num1, num2)
print(f"The sum of {num1} and {num2} is: {result}")

#function with keyword arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

# Using positional arguments and using the default greeting as Hello
print(greet("Alice"))

# Using keyword arguments to specify the greeting, doesn't have to be in order
print(greet(greeting="Welcome", name="Bob"))