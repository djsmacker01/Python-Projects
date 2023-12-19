import json

def new_employee():
    name = input("What is the new employee's name? ")
    role = input("What is the new employee's position? ")
    experience = int(input("How many years of experience does this employee have? "))
    return {"Name": name, "Role": role, "Experience": experience}

def read_json(file_path):
  
        with open(file_path, "r") as file:
            employees = json.load(file)
  
        return employees

def write_json(file_path, json_file):
    with open(file_path, "w") as file:
        json.dump(json_file, file, indent=3)

file_path = "company.json"

while True:
   
        answer = input("Do you wish to add new employee? (Y/N): ").upper()
        if answer == "N":
            break
        elif answer == "Y":
            employee_data = new_employee()
            employees_list = read_json(file_path)
            employees_list.append(employee_data)
            write_json(file_path, employees_list)
            print("Employee added successfully!")
        else:
            print("Please submit a valid answer (Y/N).")


