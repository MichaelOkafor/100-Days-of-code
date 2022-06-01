print("welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
tip = int(input("what percentage tip would you like to give? 10,15,20? "))
split_bill = int(input("how many people to split the bill with? "))
percentage_tip = (tip/100) * total_bill
bill = total_bill + percentage_tip
each_pay = bill/split_bill
round(each_pay, 2)
print(f"Each person should pay {each_pay}")