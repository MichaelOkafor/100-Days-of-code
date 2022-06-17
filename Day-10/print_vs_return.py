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

def calculator():
    num1 = int(input("Pick a number: "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation")
        num2 = int(input("What's the next number? "))
        calculator_function = operations[operation_symbol]
        answer = calculator_function(num1,num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()
calculator()