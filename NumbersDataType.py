#  Numbers data type
# Numbers have four types in Python. Int, float, complex, and long.
# int_num = 10 #int value
# float_num = 10.2 #float value
# complex_num = 3.14j #complex value
# # long_num = 1234567L #long value

# print(int_num, float_num, complex_num)

#  List Data Type
# A list contains items separated by commas and enclosed within square brackets [].lists are almost similar to arrays
# in C. One difference is that all the items belonging to a list can be of different data type

# list = [123,'abcd',10.2,'d'] #can be an array of any data type or single data type.
# list1 = ['hello','world']
# print(list) #will output whole list. [123,'abcd',10.2,'d']
# print(list[0:2]) #will output first two element of list. [123,'abcd']
# print(list1 * 2) #will gave list1 two times. ['hello','world','hello','world']
# print(list + list1) #will gave concatenation of both the lists.
# [123,'abcd',10.2,'d','hello','world']

""""
This is a multiline comment
"""


# def hello(name):
#     """Great someone.

#     print(name)
#     """
#     print('Hello '+ name)
# hello('James')

# import datetime
# dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
# print(dt)
"""
Create a Rectangle class with the following properties or parameters: base, height, and colour. By default, base and height are equal to 1.
Create the following methods:
An instance method that returns the perimeter.
An instance method that returns the area.
A method that returns true if the base is greater than a minimum value passed to it, defaulting to 5.
A str() method that returns the dimensions of the base and height.
A static method that, given two rectangles, returns true if they are equal; otherwise, it should return false.
A class method that returns an instance with random dimensions for the rectangle


class Rectangle:
    def __init__(self, base, height, colour):
        self.base = base
        self.height = height
        self.colour = colour

    def parameters(self):
        return 2 * (self.height + self.base) 

    def area(self):
"""
import random

class Rectangle:
    def __init__(self, base=1, height=1, color=""):
        self.base = base
        self.height = height
        self.color = color

    def perimeter(self):
        return 2 * (self.base + self.height)

    def area(self):
        return self.base * self.height

    def is_base_greater_than(self, min_value=5):
        return self.base > min_value

    def __str__(self):
        return f"Rectangle(base={self.base}, height={self.height}, color={self.color})"

    @staticmethod
    def are_equal(rectangle1, rectangle2):
        return rectangle1.base == rectangle2.base and rectangle1.height == rectangle2.height

    @classmethod
    def create_random_rectangle(cls):
        base = random.randint(1, 40)
        height = random.randint(1, 40)
        color = random.choice(["red", "blue", "green", "yellow"])
        return cls(base, height, color)

# Example usage:
rect1 = Rectangle()
rect2 = Rectangle(3, 4, "blue")

print(f"Perimeter of rect1: {rect1.perimeter()}")
print(f"Area of rect2: {rect2.area()}")
print(f"Is base of rect2 greater than 5? {rect2.is_base_greater_than()}")
print(f"String representation of rect1: {str(rect1)}")
print(f"Are rect1 and rect2 equal? {Rectangle.are_equal(rect1, rect2)}")

random_rect = Rectangle.create_random_rectangle()
print(f"Random rectangle: {random_rect}")
