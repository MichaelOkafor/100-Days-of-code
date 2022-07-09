for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0: #former code: had an if statement instead of an elif
        print("Fizz")
    elif number % 5 == 0: # former code: had an if statement instead of an elif
        print("Buzz")
    else:
        print(number) #former code: had the number enclosed in a square bracket[]