# *args: Many Positional Arguments. *args are type tuple
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(5, 6, 7, 8, 9))


# **kwargs: Many Key worded Arguments. **Kwargs are type dict
def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# the **kwargs can also work with classes
class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get("make")  # this is the same as kwargs["make"]. but .get returns no errors
        self.model = kwargs.get("model")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
