import random

while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()   #Lower() makes all the input lower to match the predefined choices
    if player == computer:
        print("computer:", computer)
        print("Player:", player)
        print("Tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer:", computer)
            print("Player:", player)
            print("You win!")
        else:
            print("Paper covers rock, You lose!")
        
    elif player == "paper":
        if computer == "rock":
            print("computer:", computer)
            print("Player:", player)
            print("You win!")
        else:
            print("Scissors cuts paper, You lose " )

        
    elif player == "scissors":
        if computer == "paper":
            print("computer:", computer)
            print("Player:", player)
            print("You Win!")
        else:
            print("Rock smashes scissors, You Lose!")
       
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("Bye!")
