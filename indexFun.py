# def new_job(data):
#     while True:
#         '''
#         A function that will edit the value of the job key in the json file
#         '''
#         try:
#             entry = int(input("What is the id of the friend who got new job?: "))
#             # int(entry),"The response should be enter an integer value"
#         except:
#             print(f"Please enter an integer value")
#         else:
#             entry = int(entry)
#             break



#     data[entry - 1]["job"] = input("What is the new job title?")

# def new_job(data):
#     while True:
#         try:
#             entry = int(input("What is the id of the friend who got a new job?: "))
#         except ValueError:
#             print("Error: Please enter an integer value for the friend's ID.")
#         else:
#             if 0 <= entry < len(data):
#                 break
#             else:
#                 print("Error: Invalid friend ID. Please enter a valid ID.")

#     new_job_title = input("What is the new job title?: ")
#     data[entry]["job"] = new_job_title


# create a new function called birthday, 
# the function will auto increment the age value of the selected friend by one

# def create_birthday(friend,friend_id):
#     try:
#         for friend in friend:
#             if friend["friend_id"] == friend_id:
#                 friend["age"] += 1
#                 print(f" Happy birthday, My darling {friend['name']}! You are now {friend['age']} years old. ")
#                 break
#             else:
#                 assert ValueError(f"Friend with friend_id {friend_id} not found.")
#     except Exception as e:
#         print(f"Error: {e}")

# def birthday(data):
#     while True:
#         try:
#             entry = int(input("what is the id of the friend who had a birthday?: "))  
#         except:
#             print("")   


def new_job(data):
    '''
    A function that will edit the value of the "job" key in the json file
    :param data: The json file you have imported
    :return: NA
    '''
    while True:
        try:
            entry = int(input("What is the id of the friend who got a new job?: "))
        except:
            print("Please enter an integer value")
        else:
            entry = int(entry)
            break

    data[entry - 1]["job"] = input("What is the new job title? : ")

# Create a new function called birthday, this function will automatically increment the age value of the
# selected friend by one


def birthday(data):
    while True:
        try:
            entry = int(input("What is the id of the friend who had a birthday?: "))
        except:
            print("Please enter an integer value")
        else:
            entry = int(entry)
            break

    while True:
        try:
            entry <= len(data)
        except:
            print(f"Please enter a value equal to or lower then{len(data)}")
        else:
            entry = int(entry)
            break
    data[entry - 1]["age"] += 1

def new_friend(data):
    id = data[-1]["friend_id"] + 1
    name = input("Please enter your new friends name: ")
    age = int(input("Please enter your new friends age: "))
    score = float(input("Please enter your new friends friend score: "))
    job = input("Please enter your new friends job: ")
    data.append({
        "friend_id" : id,
        "name" : name,
        "age" : age,
        "score" : score,
        "job" : job
    })