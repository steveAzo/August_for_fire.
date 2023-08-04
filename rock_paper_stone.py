import random

def get_user_choice():
    lists = ["scisscors", "paper", "rock"]
    print("Your choice can either be; rock, scisscors and paper.")
    while True:
        choice = input("Enter your choice:").lower()
        if choice in lists:
            return choice
        else:
            print("Wrong")
    
def get_computer_choice():
    choice = random.choice(["scisscors", "rock", "paper"])
    return choice

def determine_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        return "There is a tie. Give it another try to determine the winner"
    elif (user_choice == "rock" and computer_choice == "scisscors")  or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scisscors" and computer_choice == "rock"):
        return "You won🍟🌭."
    else:
        return "You lost dude😛😂. Better luck next time."

def play_game():
    print("Welcome to the Rock, Paper and Scisscors game!🤩")
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    print(f" you chose {user_choice} and the computer chose {computer_choice}")
    print(determine_winner(user_choice, computer_choice))
    
play_game()
    