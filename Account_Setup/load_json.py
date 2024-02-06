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
        text_input = input(prompt).strip()
        if text_input:
            return text_input
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

