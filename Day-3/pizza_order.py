print("welcome to the pizza deliveries")
size = input("what size of pizza do you want? S,M,L? ")
add_pepperoni = input("Do you want pepperoni? Y or N? ")
extra_cheese = input("Do you want extra cheese? Y or N? ")

bill = 0
if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
else:
    bill +=25
    if add_pepperoni =="Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your Bill is {bill}")