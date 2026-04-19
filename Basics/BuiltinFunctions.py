print("Introduce yourself!")
name = input("Enter your name: ").strip()
print(f"Hello, {name}!")

num1 = int(input("Enter first number: ").strip())
num2 = int(input("Enter second number: ").strip())
options = input("Chose an operation: + - * / : ").strip()

if options == "+":
    result = num1 + num2
elif options == "-":
    result = num1 - num2
elif options == "*":
    result = num1 * num2
elif options == "/":
    result = num1 / num2
else:    
    print("Invalid operation selected.")
    result = None

print(f"The result of {num1} and {num2} is: {result}")