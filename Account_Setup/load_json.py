import json

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, "r") as file:
        return json.load(file)

def save_json(file_path, data):
    """Save JSON data to a file."""
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)


def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading JSON from {file_path}: {e}")
        return None

def save_json(file_path, data):
    """Save JSON data to a file."""
    try:
        with open(file_path, "w") as outfile:
            json.dump(data, outfile, indent=4)
    except (PermissionError, OSError) as e:
        print(f"Error saving JSON to {file_path}: {e}")


def input_text(prompt):
    """Get valid text input from the user."""
    while True:
        input_text = input(prompt).strip()
        if input_text:
            return input_text
        else:
            print("Error: Text input must contain at least one character.")

def numeric_input(prompt):
    """Get valid numeric input (integer) from the user."""
    while True:
        numeric_input = input(prompt)
        try:
            numeric_input = int(numeric_input)
            return numeric_input
        except ValueError:
            print("Error: Please enter a valid integer.")



first_name = input_text("Enter first name: ")
last_name = input_text("Enter last name: ")

account_no = numeric_input("Enter account number: ")
sort_code = numeric_input("Enter sort code: ")
initial_balance = numeric_input("Enter initial balance: ")

print("User input:")
print(f"First Name: {first_name}")
print(f"Last Name: {last_name}")
print(f"Account Number: {account_no}")
print(f"Sort Code: {sort_code}")
print(f"Initial Balance: {initial_balance}")



import json

def load_json(file_path):
    """Load JSON data from a file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(file_path, data):
    """Save JSON data to a file."""
    with open(file_path, "w") as outfile:
        json.dump(data, outfile, indent=4)

def input_text(prompt):
    """Get valid text input from the user."""
    while True:
        input_text  = input(prompt).strip()
        if input_text:
            return input_text
        else:
            print("Error: Text input must contain at least one character.")

def numeric_input(prompt):
    """Get valid numeric input (integer) from the user."""
    while True:
        numeric_input = input(prompt)
        try:
            numeric_input = int(numeric_input)
            return numeric_input
        except ValueError:
            print("Error: Please enter a valid integer.")

def create_new_account():
    """Create a new account entry."""
    accounts_data = load_json("accounts.json")

    # Generate a new entry ID
    new_entry_id = 1 if not accounts_data else max(account["id"] for account in accounts_data) + 1

    # Obtain user inputs
    first_name = get_input_text("Enter first name: ")
    last_name = get_input_text("Enter last name: ")
    account_no_sort_code = get_numeric_input("Enter account number: "), get_numeric_input("Enter sort code: ")
    initial_balance = get_numeric_input("Enter initial balance: ")

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

# Invoke the create_account function to create a new account
create_new_account()


def main():
    while True:
        print("\nMenu:")
        print("1. Remove account")
        print("2. Add Interest")
        print("3. Add New Account")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            # Implement account removal logic here
            pass
        elif choice == "2":
            # Implement add interest logic here
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
