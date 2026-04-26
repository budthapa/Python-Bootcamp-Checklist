from ClassesAndObjects.Person import Person


class Employee(Person):

    # invoking the constructor of the parent class
    def __int__(self):
        super().__init__("Max")
    
    def wake_up(self):
        print(f"{self._name} wakes up at 6 am")

    # method overriding
    def sleep(self):
        print("sleep from child class")


p = Person("Marie")
p.running()
p.sleep()  # method from parent class

e = Employee("Jane")
e.wake_up()
print(e._name)
e.sleep()  # method from child class
