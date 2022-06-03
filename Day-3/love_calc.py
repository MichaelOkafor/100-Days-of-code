print("Welcome to the love Calculator! ")
name1 = input("what is your name? \n").lower()
name2 = input("waht is her name? \n").lower()

add_name = name1 + name2
count_T = add_name.count("t")
count_R = add_name.count("r")
count_U = add_name.count("u")
count_E = add_name.count("e")
count_L = add_name.count("l")
count_O = add_name.count("o")
count_V = add_name.count("v")

true_count = count_T + count_R + count_U + count_E
love_count = count_L + count_O + count_V + count_E

love_score = int(true_count) + int(love_count)
if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright")
else:
    print(f"Your score is {love_score}")