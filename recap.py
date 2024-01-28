while True:
    try:
        assert input("Please type the word success: ") == "success", 'Please type the word "success"'
    except AssertionError as e:
        print(f"Error: {e}")
    else:
        print("Thank you for typing Success")
        break
    finally:
        print("The program was successfully")
print("Success Typed!!!")            