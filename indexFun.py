def new_job(data):
    while True:
        '''
        A function that will edit the value of the job key in the json file
        '''
        try:
            entry = int(input("What is the id of the friend who got new job?: "))
            # int(entry),"The response should be enter an integer value"
        except:
            print(f"Please enter an integer value")
        else:
            entry = int(entry)
            break



    data[entry - 1]["job"] = input("What is the new job title?")

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
