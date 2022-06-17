def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2

operations = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide,
}

num1 = int(input("Type a number: "))

for symbol in operations:
    print (symbol)
operation_symbol = input("select an operation from above: ")

num2 = int(input("Type a number: "))

calc_function = operations[operation_symbol]
answer = calc_function(num1,num2)
print(f"{num1}{operation_symbol}{num2} = {answer}")