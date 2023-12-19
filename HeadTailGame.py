import random

# coin_flip = input("Did the coin land on heads or tails? ")

# if coin_flip == "heads":
#     print("The coin land on heads! You Win!")
# elif coin_flip == "tails":
#     print("The coin land on tails! You lose!")

# else:
#     print("Please enter a valid answer")    
# print(coin_flip)    

# using random function
print("Welcome to the head and tail Game")

user_Player = input("Enter your guess (heads or tails): ").lower()

if user_Player not in ['heads','tails']:  
    print("Invalid input. Please enter 'heads' or 'tails'. ")

else:
    # Flip the coin
    coin_result = random.choice(['heads', 'tails'])   

    # display the result
    print(f"The coin landed on : {coin_result.capitalize()}")

    #  check if user guess correctly

    if user_Player == coin_result:
        print("Congratulations! you guessed correctly")

    else:
        print("Oops! You guessed incorrectly")   


