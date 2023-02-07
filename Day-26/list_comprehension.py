# for loop
numbers = [1, 2, 3]
new_num = []
for n in numbers:
    add_1 = n + 1
    new_num.append(add_1)

# using list comprehension
new_list = [n + 1 for n in numbers]  # [item_list for item in list]

# string as list
name = "Michael"
letter_list = [letter for letter in name]

# Range as list
range_list = [n * 2 for n in range(1, 5)]

# conditional list comprehension
names = ["Sheldon", "Amy", "Rajesh", "Penny"]
short_names = [n for n in names if len(n) < 7]
long_names = [n.upper() for n in names if len(n) > 4]
