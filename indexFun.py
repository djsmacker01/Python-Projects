def new_job(data):
    while True:
        entry = input("What is the id of the friend who got new job?: ")
        try:
            int(entry),"The response should be enter an integer value"
        except TypeError as e:
            print(f"Error: {e}")
        else:
            entry = int(entry)
            break



    data[entry - 1]["job"] = input("What is the new job title?")