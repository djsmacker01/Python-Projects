# myList = [2,4,"Matthew", True, "John"]

# print(f"Here is a list Object {myList}" )
# print(myList[2])

a = [1,2,3,4]
b = [5,6,7,8,9]

a.extend(b)
a.join(b)
print(a)

fruits = ['apple', 'banana', 'cherry']
index = fruits.index('banana')
print(index)  # Output: 1
