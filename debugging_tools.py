# def profile(firstname,lastname):
#     full_name = f"{firstname} {lastname}"
#     print("Full Name :",full_name)


# firstname = 'Smith'
# lastname = 'Mathew'
# profile(firstname,lastname)

# def profile(firstname,lastname):
#     return f"{firstname} {lastname}"

# print(profile('smith', 'Jackson'))   

num1 = 0
num2 = 10

while num1 <= num2:
    num1 += 1
    num2 *= 1

    if num1 == 5:
        num2 *=2
        continue
    print('Task Completed')