# import json
# import indexFun as pf

# with open("main.json", "r+") as open_json:
#     friends = json.load(open_json)

# # pf.new_job(friends)
# # pf.create_birthday(friends, friend_id = 1)
# choice = input ("Would yo")
# print(friends)  
# with open("main.json", "w") as write_json:
#     edited_json = json.dumps(friends,indent = 5)
#     write_json.write(edited_json)
# import json

# # Open the JSON file for reading
# with open("main.json", "r") as open_json:
#     # Load the JSON data
#     friends = json.load(open_json)

# # Now, 'friends' contains the parsed JSON content

# # Print each dictionary separately using a for loop
# for friend in friends:
#     print("Name:", friend["name"])
#     print("Age:", friend["age"])
#     print("Friend Score:", friend["friend_score"])
#     print("Job:", friend["job"])
#     print("---")


# for friend in friends:
#     print(friend)    


# Print off the two dictionaries separetely using a for loop


import json
import practice_funcs as pf

with open("friends.json", "r+") as open_json:
    friends = json.load(open_json)


choice = input("Would you like to change a job, have a birthday or add a friend? \n enter 'job' or 'birthday' or 'friend': ")

if choice == "job":
    pf.new_job(friends)
elif choice == "birthday":
    pf.birthday(friends)
elif choice == "friend":
    pf.new_friend(friends)
else:
    print("Please enter a valid answer")

print(friends)


pf.new_friend(friends)


with open("friends.json", "w") as write_json:
    edited_json = json.dumps(friends, indent = 4)
    write_json.write(edited_json)