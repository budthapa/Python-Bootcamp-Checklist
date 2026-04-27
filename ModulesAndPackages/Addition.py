# __name__ always prints the name of the module if run from the same file,
# but it will print the module name if run from another file
print(__file__, __name__)


class Addition:
    def add(self, a, b):
        print("This will calculate sum")
        print(a + b)


def sum_three(a, b, c):
    print(a + b + c)
