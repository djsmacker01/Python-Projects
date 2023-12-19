import json

def read_student_profile(StudentProfile):

    with open(StudentProfile, "r") as file:
        student_profile = json.load(file)
    return student_profile

def write_student_profile(StudentProfile, new_student):
    
    student_profile = read_student_profile(StudentProfile)
    student_profile.append(new_student)
    with open(StudentProfile, "w") as file:
        json.dump(student_profile, file, indent=7)


new_student_data = {
    "student_id": 7,
    "student_name": "Max Cox",
    "Date_of_Birth": "1990-01-23",
    "Gender": "Female",
    "Department": "Science"
}

StudentProfile = "StudentProfile.json"

write_student_profile(StudentProfile, new_student_data)
print(read_student_profile(StudentProfile))
