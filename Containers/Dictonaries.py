# similar to Map in Java with a key value pair
days = {
    "sun": "Sunday",
    "mon": "Monday",
    "tue": "Tuesday",
    "wed": "Wednesday",
    "thu": "Thursday",
    "fri": "Friday",
}
print(type(days))
print(days)
print(len(days))

print(days["wed"])
days.update({"sat": "Saturday"})
print(days)
print(len(days))


# iterations
for value in days.values():
    print(value)

for key in days.keys():
    print(key)

for day in days:
    print(day, days[day])

for day in days.items():
    print(day)

for key, value in days.items():
    print(key, value)

# removing items
del days["mon"]
print(days)
print(days.pop("sun"))
print(days.popitem())
print(days)


keys = days.keys()
print(keys)

values = days.values()
print(values)

del days["tue"]
print(days)

# get item from dict, this will return the value
print(days.get("wed"))

print(days)

# return the default value if the item doesn't exist
mon = days.get("mon", "Default value")
print(mon)
