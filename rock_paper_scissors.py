from random import randint

# Create a list of string variables that will be the play options
command = ["Rock", "Paper", "Scissors"]

# Assign a random play to the computer*
computer = command[randint(0,2)]

# Set player variable to boolean value False
player = False

while player == False:
# Set player to True - Why? : 
# Once the while loop starts, the computer will patiently wait for you to make a play.
# As soon as you take your turn, your status changes from False to True because any value assigned to the variable player makes player True.
    player = input("Rock, Paper, Scissors? ")
# Use nested if/elif/else statements to check every possible outcome and choose the winner
    if player == computer:
        print("Tie!")
    elif player == "Rock":
        if computer == "Paper":
            print("You lose!, Paper beats Rock!")
        else:
            print("You win! Rock beats Scissors!")
    elif player == "Paper":
        if computer == "Rock":
            print("You win! Paper beats Rock!")
        else:
            print("You lose! Scissors beats Paper!")
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose! Rock beats Scissors!")
        else:
            print("You win! Scissors beats Paper!")
    else:
        print("That's not a valid play! Check your spelling")
    # To continue the loop, set player to False again
    player = False
    computer = command[randint(0,2)]
