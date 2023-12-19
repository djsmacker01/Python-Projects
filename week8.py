import json 


# with open("Employee.json", "r") as file:
#     employees = json.load(file)

# print(type(employees[0]))

# employees.append({"Name": "Daniel", "Role": "Tutor", "Time at Iungo": 1})

# with open("Employee.json", "w") as file:
#     json.dump(employees,file,indent=4)

with open("StudentProfile.json", "r") as file:
    student_profile = json.load(file)

student_profile.append(
    {       "student_id": 6,
            "student_name": " Max Cox",
            "Date_of_Birth": "1990-01-23",
            "Gender": "Female",
            "Department": "Science"
            
            }
            )
with open("StudentProfile.json", "w") as file:  
    json.dump(student_profile,file,indent=7) 

print(student_profile)        