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
# print("Welcome to the head and tail Game")

# user_Player = input("Enter your guess (heads or tails): ").lower()

# if user_Player not in ['heads','tails']:  
#     print("Invalid input. Please enter 'heads' or 'tails'. ")

# else:
#     # Flip the coin
#     coin_result = random.choice(['heads', 'tails'])   

#     # display the result
#     print(f"The coin landed on : {coin_result.capitalize()}")

#     #  check if user guess correctly

#     if user_Player == coin_result:
#         print("Congratulations! you guessed correctly")

#     else:
#         print("Oops! You guessed incorrectly")   

#  Favourite number       

# fav_num = input("Enter your Favourite number")

# fav_num_int = int(fav_num)

# print(f"Your favourite number is {fav_num_int * 3}" )


team_1 = input("What is the name of the first team: ")
team_2 = input("What is the name of the second team: ")
team_1_score = int(input(f"What was the {team_1}'s score?: "))
team_2_score = int(input(f"What was the {team_2}'s score?: "))

if team_1_score > team_2_score:
    print(f"{team_1} won the game by {team_1_score}: {team_2_score}")
elif team_1_score < team_2_score:
    print(f"{team_2} won the game by {team_2_score}: {team_1_score}")

else:
    print(f"The game ended with {team_1_score}: {team_2_score} draw")