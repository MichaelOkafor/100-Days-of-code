print("Welcome to the Treasure Island. \nYour mission is to find the Treasure.")
choice1 = input('You are at a cross road. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'left':
    choice2 = input("You came to a lake. There is an Island in the middle of the lake. Type 'wait' to wait for a boat or type 'swim' to swim across. \n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the Island unharmed. There is a house with 3 doors. One 'Red', one 'Yellow', and one 'Blue'. Which one do you chose? \n").lower()
        if choice3 == "yellow":
            print("You found the treasure. You win")
        elif choice3 == "blue":
            print("You entered a room of Beasts. Game Over.")
        elif choice3 == "red":
            print("Its a room full of fire. Game Over")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print("You got attacked by an angry trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")