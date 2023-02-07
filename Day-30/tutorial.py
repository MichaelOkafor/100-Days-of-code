# error handling
try:
    file = open("data.txt")
    a_dict = {"key": "value"}
    print(a_dict["non_existent_key"])
except FileNotFoundError:  # the except keyword allows you to specify the error you want to catch
    file = open("data.txt")
    file.write("something")
except KeyError as error_message:  # you can save the error message. Except works if the code under try: fails
    print(f" The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:  # this keyword works no matter what happens
    file.close()
    print("The file was closed")


# Raising exceptions/errors (using the raise keyword)
# Raising exception's means creating your own error messages because the code may look like a valid code,
# but may have some underlying bugs underneath. example B.M.I code

height = float(input("Height(m): "))
weight = int(input("Weight(m)"))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")
bmi = weight/height**2
print(bmi)
