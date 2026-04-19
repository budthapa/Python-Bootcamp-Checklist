# boolean are uppercase in python, eg: True and False

sunny = True
base_temperature = 15
temperature = int(input("What's the temperature today? ").strip())

if sunny and temperature > base_temperature:
    print("It's a nice day!")
elif sunny and temperature >= 5 and temperature <= base_temperature:
    print("It's a sunny but cold day!")
elif sunny and temperature < 5:
    print("It's a sunny but very cold day!")
else:    
    print("It's a cold and cloudy day!")