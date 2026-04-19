#range(1, 11) generates a sequence of numbers from 1 to 10 (11 is not included)
for n in range(1, 11):
    print(n)

#range(1, 11, 2) generates a sequence of numbers from 1 to 10 with a step of 2 (11 is not included)
for n in range(1, 11, 2):
    print(n)

for n in range(50, 40, -1):
    print(n)

for num, index in enumerate(range(1, 11)):
    print(f"Number: {num}, Index: {index}")