fruits = ["Apple", "Pear", "Orange"]


# catch the exception and make sure the code works
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + " pie")


make_pie(4)
