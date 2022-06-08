word_list = ["ardvark", "babbon", "camel"]

import random
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

# create blanks
display = []
for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter ").lower()

    # if user has entered a letter they already guessed print the letter and let the know.
    if guess in display:
        print(f"You have already guessed {guess}")

    # check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"current position: {position}\n current letter: {letter}\n guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # check if user is wrong
    if guess not in chosen_word:
        # if letter is not in chosen_word print out the letter and let the user know
        lives -= 1
        print(f"You guessed {guess}, that was not in the chosen word. You lose a life")
        if lives == 0:
            end_of_game = True
            print("You Lose")

    # join all elements in the display and turn it into a string 
    print(f"{' '.join(display)}")

    # check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You Win")