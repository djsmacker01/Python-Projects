counter = 0

while True:
    counter += 1
    result = input(f"This loop has run {counter} times, would you like to continue Y/N?: ").upper()
    if result == "N":
        break
    elif result == "Y":
        continue
    else:
        print("Please submit a valid response")    
