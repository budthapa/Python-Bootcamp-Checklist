class Vehicle:
    count = 0

    def __init__(self, name=""):
        self._name = name
        Vehicle.count += 1

    def drive(self):
        print(f"{self._name} Drives BMW")


Vehicle()
Vehicle()
Vehicle()
Vehicle()
Vehicle()
print(Vehicle.count)
