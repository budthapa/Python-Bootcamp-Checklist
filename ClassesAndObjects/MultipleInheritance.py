#  Python supports multiple inheritance, but java doesn't
#  we basically use interface in java
from ClassesAndObjects.ClassProperties import Vehicle
from ClassesAndObjects.Inheritance import Employee


# extending both the classes from the child class
class Company(Employee, Vehicle):
    def __init__(self, name):
        super().__init__(name)


c = Company("Rita")
c.sleep()
c.wake_up()
c.drive()

