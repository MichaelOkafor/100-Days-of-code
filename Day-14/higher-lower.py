from game_data import data
import random

def format_data(account):
    '''takes the account data and return the printable format'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Takes the users guess and follower count and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# keep track of the score
score = 0
game_should_continue = True
account_b = random.choice(data)

# make the game repeatable
while game_should_continue:
    # generate a random account from game data

    # making the account at position B become the next account at position A
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Against B: {format_data(account_b)}")

    # ask the user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    ## get the follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guesses
    ## keep track of the score
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that is wrong. Final score: {score}")

    # clear the screen between rounds