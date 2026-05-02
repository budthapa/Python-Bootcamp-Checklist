def is_armstrong_number(number):
    digit = str(number)
    power = len(digit)
          
    return sum(int(num) ** power for num in digit) == number
    
