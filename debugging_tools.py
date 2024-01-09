# def profile(firstname,lastname):
#     full_name = f"{firstname} {lastname}"
#     print("Full Name :",full_name)


# firstname = 'Smith'
# lastname = 'Mathew'
# profile(firstname,lastname)

# def profile(firstname,lastname):
#     return f"{firstname} {lastname}"

# print(profile('smith', 'Jackson'))   

# num1 = 0
# num2 = 10

# while num1 <= num2:
#     num1 += 1
#     num2 *= 1

#     if num1 == 5:
#         num2 *=2
#         continue
#     print('Task Completed')

#     # Print a 3 times multiplication table
# for i in range(1, 13):
#     result = 3 * i
#     print(f"3 x {i} = {result}")


# 

def highestNumber(num):
    if not num:
        return f" Not a number"

    highest = num[0]    

    for i in num:
        if i > highest:
            highest = i
    return highest

num_list = [78,20,30,40,100,60,]        
output = highestNumber(num_list)
print (f"Highest number is: {output}")