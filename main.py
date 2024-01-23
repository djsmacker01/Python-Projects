import json

with open("main.json", "r+") as open_json:
    friends = json.load(open_json)

print(friends)  
import json

# Open the JSON file for reading
with open("main.json", "r") as open_json:
    # Load the JSON data
    friends = json.load(open_json)

# Now, 'friends' contains the parsed JSON content

# Print each dictionary separately using a for loop
for friend in friends:
    print("Name:", friend["name"])
    print("Age:", friend["age"])
    print("Friend Score:", friend["friend_score"])
    print("Job:", friend["job"])
    print("---")


for friend in friends:
    print(friend)    


# Print off the two dictionaries separetely using a for loop