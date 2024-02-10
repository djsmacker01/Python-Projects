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
            # Account removed
            return True  
            # Account not found
    return False  

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

# File: main.py

import json

# Function to load JSON data from a file
def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save JSON data to a file
def save_json(file_path, data):
    """Save JSON data to a file."""
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)

# Function to get valid text input from the user
def input_text(prompt):
    """Get valid text input from the user."""
    while True:
        text_input = input(prompt).strip()
        if text_input:
            return text_input
        else:
            print("Error: Text input must contain at least one character.")

# Function to get valid numeric input (integer) from the user
def numeric_input(prompt):
    """Get valid numeric input (integer) from the user."""
    while True:
        numeric_input = input(prompt)
        try:
            numeric_input = int(numeric_input)
            return numeric_input
        except ValueError:
            print("Error: Please enter a valid integer.")

# Function to create a new account entry
def create_new_account():
    """Create a new account entry."""
    accounts_data = load_json("accounts.json")

    # Generate a new entry ID
    new_entry_id = 1 if not accounts_data else max(account["id"] for account in accounts_data) + 1

    # Obtain user inputs
    first_name = input_text("Enter first name: ")
    last_name = input_text("Enter last name: ")
    account_no_sort_code = numeric_input("Enter account number: "), get_numeric_input("Enter sort code: ")
    initial_balance = numeric_input("Enter initial balance: ")

    # Create new account entry
    new_account = {
        "id": new_entry_id,
        "first_name": first_name,
        "last_name": last_name,
        "account-no/sort_code": account_no_sort_code,
        "balance": initial_balance
    }

    # Add the new account to the existing data
    accounts_data.append(new_account)

    # Save the updated data
    save_json("accounts.json", accounts_data)

    print("New account entry created successfully!")

# Main program
def main():
    while True:
        # Display menu options
        # ...

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Implement account removal logic here
            pass
        elif choice == "2":
            # Implement add interest logic here to perform the account deletion
            pass
        elif choice == "3":
            create_new_account()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
