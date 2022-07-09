import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

turns = 0

# function to check the user's guess against the actual answer
def check_answer(guess, answer, turns):
    """ Checks answer against guess. Returns the number of turns remaining """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it. The answer was {answer}")

# make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choosing a random number between 1 and 100
    print ("Welcome to the number guessing game")
    print ("I am thinking of a number between 1 and 100")
    answer = random.randint(1,100)
    print(f"Psst, the answer is {answer}") # this is done to test the code.

    turns = set_difficulty()

    guess = 0
    # Repeat the guessing functionality if they get it wrong
    while guess != answer:
        print(f"You have {turns} attempts to guess the number")
        # let the user guess a number
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")
game()