str1 = "Hello"
str2 = "hello"

# Case-sensitive comparison
if str1 == str2:
    print("The strings are equal (case-sensitive).")
else:    
    print("The strings are not equal (case-sensitive).")

# Case-insensitive comparison
if str1.lower() == str2.lower():
    print("The strings are equal (case-insensitive).")
else:    
    print("The strings are not equal (case-insensitive).") 

# Lexicographical comparison
animal1 = "elephant"
animal2 = "Dog"

if animal1 < animal2:
    print(f"{animal1} comes before {animal2} in lexicographical order.")
else:
    print(f"{animal1} does not come before {animal2} in lexicographical order.")