class Person:
    # define constructor and pass an attribute called name
    # __init__ is the standard name for constructor
    def __init__(self, name):
        self._name = name
        print(f"got name {self._name}")

    def running(self):  # self is similar to this in java
        print(f"{self._name} is running")

    def sleep(self):
        print(f"{self._name} is sleeping")

    # changing object to string
    def __str__(self):
        return f"This is a string representation for object with param: {self._name}"


p = Person("John")
print(type(p))
print(p.running())

# calling the string method
print(p.__str__())
# or we can simply use
print(str(p))

