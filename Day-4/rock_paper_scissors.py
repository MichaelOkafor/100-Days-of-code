from random import randint

rock = "rock"
paper = "paper"
scissors = "scissors"

game_images = [rock, paper, scissors]
user_choice = int(input("what do you want to choose? Type 0 for Rock, 1 for Paper, 2 for Scissors "))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose! ")
else:
    print(game_images[user_choice])

    computer_choice = randint(0,2)
    print("computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Win")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a draw")