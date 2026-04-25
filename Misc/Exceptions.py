# exceptions are similar to try catch finally in java
try:
    print(1 / 0)
except:
    print("Something failed")
finally:
    print("Finally executed")


# catching the exact message of exception
try:
    print(20 / 0)
except Exception as ex:
    print(ex)
finally:
    print("program exit")

# type of exception
try:
    data = {}
    data["same"]

    print(100/0)
except ZeroDivisionError as zero:
    print(zero)
    print(type(zero))
except Exception as ex:
    print(ex)
    print(type(ex))

