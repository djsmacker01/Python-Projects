# import json

# x = input("1. Remove account  2. Add Interest: ")
# if x == "1":
#     with open("Data/accounts.json", "r+") as infile:
#         accounts = json.load(infile)
#     idToRemove = int(input("Enter the ID of the account to remove: "))
#     for Account in accounts:
#         if Account["id"] == idToRemove:
#             accounts.remove(Account)
#     with open("Data/accounts_updated.json", "w") as outfile:
#         accs_as_json = json.dumps(accounts, indent=4)
#         outfile.write(accs_as_json)
# elif x == "2":
#                 with open("Data/accounts.json", "r+") as infile:
#                     ACCOUNTS = json.load(infile)
#                 interest_rate = float(input("Enter an interest rate e.g. 2.5: "))
#                 for acc in ACCOUNTS:
#                     acc["balance"] *= (1 + (interest_rate/100))
#                 with open("Data/accounts_with_interest.json", "w") as outfile:
#                     accounts_converted_to_json_format_ = json.dumps(ACCOUNTS, indent=4)
#                     outfile.write(accounts_converted_to_json_format_)




import json
#function that take in two arguments
def remove_account(accounts, id_to_remove):
    for account in accounts:
        if account["id"] == id_to_remove:
            accounts.remove(account)
            return True  # Account removed
    return False  # Account not found

def add_interest(accounts, interest_rate):
    for account in accounts:
        account["balance"] *= (1 + (interest_rate / 100))

# Read JSON data
with open("Account_Setup/account.json", "r") as file:
    accounts_data = json.load(file)

# User input
choice = input("1. Remove account  2. Add Interest: ")

if choice == "1":
    id_to_remove = int(input("Enter the ID of the account to remove: "))
    if remove_account(accounts_data, id_to_remove):
        print(f"Account with ID {id_to_remove} removed.")
    else:
        print(f"Account with ID {id_to_remove} not found.")
else:
    interest_rate = float(input("Enter an interest rate e.g. 2.5: "))
    add_interest(accounts_data, interest_rate)

# Write changes back to the original file
with open("Account_Setup/account.json", "w") as outfile:
    accounts_as_json = json.dumps(accounts_data, indent=4)
    outfile.write(accounts_as_json)
