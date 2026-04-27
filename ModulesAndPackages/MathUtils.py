import ModulesAndPackages  # full import
from ModulesAndPackages.Addition import Addition  # partial import


class MathUtils:
    def __init__(self):
        print("init constructor")
        self.add()
        print(__file__, __name__)

    def add(self):
        sum = Addition()
        sum.add(2, 3)


MathUtils()
ModulesAndPackages.Addition.sum_three(10, 20, 30)
