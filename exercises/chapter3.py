"""
Wrote for Python 3.10

Chapter 3.

Part 1
Create a function which receives 3 integers and sum them
Call that function from main() and give it 3 values

Part 2.
Create a Car class
Inside Car class, a property that contains the number of doors
A method that increases the number of doors
Inside main(), create Mycar object and add a door
Display the number of doors in the
"""


def main():
    print(my_sum(1, 2, 3))

    mycar = Car()
    mycar.addadoor()
    print(mycar.ndoors)


def my_sum(value1, value2, value3):
    return value1 + value2 + value3


class Car:
    def __init__(self):
        self.ndoors = 4

    def addadoor(self):
        self.ndoors += 1


if __name__ == "__main__":
    main()
