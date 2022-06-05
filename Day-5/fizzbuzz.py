for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
    elif number % 3:
        print("fizz")
    elif number % 5:
        print("buzz")
    else:
        print(number)