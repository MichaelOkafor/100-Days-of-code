names_string = input("Give me everybody's names, seperated by a comma: ")
names = names_string.split(",")

import random
rand_choice = random.randint(0, (len(names)-1))
person = names[rand_choice]
print(f"{person} will pay for today's meal")