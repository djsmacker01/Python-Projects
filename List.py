# myList = [2,4,"Matthew", True, "John"]

# print(f"Here is a list Object {myList}" )
# print(myList[2])

a = [1,2,3,4]
b = [5,6,7,8,9]

a.extend(b)
# a.join(b)
print(a)

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)  # Output: ['cherry', 'banana', 'apple']

# To find the maximum number
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
max_value = max(numbers)
print(max_value)  # Output: 9
print("--------- Find the Minimum Value---------")
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
min_value = min(numbers)
print(min_value)  # Output: 9


print("------ Sorted Function-----") # Output:
fruits = ['Grape', 'apple', 'banana', 'cherry']
sorted_fruits = sorted(fruits)
print(sorted_fruits)  # Output: ['apple', 'banana', 'cherry']
