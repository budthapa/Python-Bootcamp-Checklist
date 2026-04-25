# create a custom exception class and raise the eception
class MyException(Exception):
    pass


try:
    raise MyException("Something went bad")
except MyException as ex:
    print(ex)  # this will print the exception message passed from raise MyException("message here")
