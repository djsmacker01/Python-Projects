# # def profile(firstname,lastname):
# #     full_name = f"{firstname} {lastname}"
# #     print("Full Name :",full_name)


# # firstname = 'Smith'
# # lastname = 'Mathew'
# # profile(firstname,lastname)

# # def profile(firstname,lastname):
# #     return f"{firstname} {lastname}"

# # print(profile('smith', 'Jackson'))   

# # num1 = 0
# # num2 = 10

# # while num1 <= num2:
# #     num1 += 1
# #     num2 *= 1

# #     if num1 == 5:
# #         num2 *=2
# #         continue
# #     print('Task Completed')

# #     # Print a 3 times multiplication table
# # for i in range(1, 13):
# #     result = 3 * i
# #     print(f"3 x {i} = {result}")


# # 

# def highestNumber(num):
#     if not num:
#         return f" Not a number"

#     highest = num[0]    

#     for i in num:
#         if i > highest:
#             highest = i
#     return highest

# num_list = [78,20,30,40,100,60,]        
# output = highestNumber(num_list)
# print (f"Highest number is: {output}")

# # Try and effect error handling

# def division(a,b):
#     return (a/b)

# try:
#     result = division(10, 2)

# except Exception as e:
#     print(f"Error: {e}")

# else:
#     print("Code run successfully")

# finally:
#     print("This code can execute")



# Create some code that will calculate the average number i a list

# def average_number(number):
#     result = sum(number)
#     average = result / len(number)
#     return average

# num_list = [26,56,23,55,23,1,34,2,3,65,]
# print(f"Average number is:" average_number(num_list)") 

def average_number(numbers):
    result = sum(numbers)
    average = result / len(numbers)
    return average

num_list = [26, 56, 23, 55, 23, 1, 34, 2, 3, 65]
try:
    assert len(num_list) > 0, "num_list should contain entries"
except AssertionError as e:
    print(f"Error: {e}")

try:
    assert type(num_list) is list, "The inputeed should be list"  
except AssertionError as e:
    print(f"Error: {e}")         
# 

# try:
#     result = average_number(num_list)
#     print(f"Average number is: {result}")
# except Exception as error:
#     print(f"Error: {error}")

# empty_list = []
# try:
#     result = average_number(empty_list)
#     print(f"Average number is: {result}")
# except ValueError as ve:
#     print(f"Error: {ve}")    

# Test the average number function, test to see if the list is empty and also if the inputted list is list
# assert type(num_list) is list, "Number of numbers"

# def average_number(numbers):
#     if not isinstance(numbers, list):
#         raise ValueError("Input must be a list")
    
#     if not numbers:
#         raise ValueError("List cannot be empty")

#     result = sum(numbers)
#     average = result / len(numbers)
#     return average

# # Test with a valid list
# num_list = [26, 56, 23, 55, 23, 1, 34, 2, 3, 65]
# try:
#     result = average_number(num_list)
#     print(f"Average number is: {result}")
# except ValueError as ve:
#     print(f"Error: {ve}")

# # Test with an empty list
# empty_list = []
# try:
#     result = average_number(empty_list)
#     print(f"Average number is: {result}")
# except ValueError as ve:
#     print(f"Error: {ve}")

# # Test with a non-list input
# non_list_input = 42
# try:
#     result = average_number(non_list_input)
#     print(f"Average number is: {result}")
# except ValueError as ve:
#     print(f"Error: {ve}")

