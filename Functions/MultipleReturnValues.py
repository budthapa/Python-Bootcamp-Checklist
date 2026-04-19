# show how we can use multiple return values from the function
def countries():
    return "Nepal", "China", "India", "Bhutan"  # return tuple


countries = countries()

print(type(countries))  # this will display tuple
print(countries)

# unpacking the tuples
# left variables should be of exact size of the returned tuples, or it will throw runtime-exception
# ValueError: too many values to unpack error
country1, country2, country3, country4 = countries
print(country1, country2, country3, country4)
