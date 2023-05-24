import random

losses = 0
wins = 0
ties = 0
arsenal = ["rock", "paper", "scissors"]
end = ["quit", "stop", "exit", "end"]
choices = arsenal + end

while True:

    user_select = input("Enter a choice (rock, paper, scissors, quit): ").lower()

    while user_select not in choices:
        print(f"\n\"{user_select}\" is not a valid selection. Please try again -\n")
        user_select = input("Enter a choice (rock, paper, scissors): ").lower()
        
    if user_select in end:
        print(f"\nFinal Score:\nWins: {wins}\nLosses: {losses}\nTies: {ties}\n\n")
        if losses == 0 and wins == 0 and ties == 0:
            print("Geez. Do you even play Rock, Paper, Scissors?")
        elif losses == wins:
            print("You tied with the computer!")
        elif losses > wins:
            print("You lost the tournament.")
        else:
            print("You won the tournament!")
        break
   
    computer_select = random.choice(arsenal).lower()
    
    print(f"\nYou chose {user_select}.\nComputer chose {computer_select}.\n\n")
        
    if user_select == computer_select:
        print(f"Both players selected {user_select}. It's a tie!\n")
        ties += 1
    elif user_select == "rock":
        if computer_select == "scissors":
            print("Rock smashes scissors! You win!\n")
            wins += 1
        else:
            print("Paper covers rock! You lose.\n")
            losses += 1
    elif user_select == "paper":
        if computer_select == "rock":
            print("Paper covers rock! You win!\n")
            wins += 1
        else:
            print("Scissors cuts paper! You lose.\n")
            losses += 1
    elif user_select == "scissors":
        if computer_select == "paper":
            print("Scissors cuts paper! You win!\n")
            wins += 1
        else:
            print("Rock smashes scissors! You lose.\n")
            losses +=1