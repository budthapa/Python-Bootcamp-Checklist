number = 0

while number < 5:
    
    number += 1
    print(f"Current number: {number}")
    
    if number == 2:
        print("Number is 2, skipping the rest of the loop.")
        continue

    if number == 4:
        print("Number is 3, breaking the loop.")
        break

    