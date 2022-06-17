def my_function():
    return 3*2
output = my_function()
print(output)

# Functions with output
def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name}{formatted_l_name}"
print(format_name("MICHAEL ", "okafor"))