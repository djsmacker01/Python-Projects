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

import datetime
dt = datetime.datetime.strptime("2016-04-15T08:27:18-0500", "%Y-%m-%dT%H:%M:%S%z")
print(dt)


