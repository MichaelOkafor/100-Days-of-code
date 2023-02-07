from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Labels
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.pack()  # pack() can take variables like side, extend etc...


# Button
def button_clicked():
    new_text = Input.get()  # this returns the Entry string
    my_label.config(text=new_text)  # this updates the text in label
    print("i got clicked")


# calls button_clicked() when pressed
button = Button(text="Click Me", command=button_clicked)  # the command detects if the calculate_button has been clicked
button.pack()


# Entries
Input = Entry(width=30)
Input.insert(END, string="Some text to begin with.")
Input.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in the text
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text miles_input")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    """gets the current value in spinbox"""
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    """prints 1 if on calculate_button is checked otherwise 0"""
    print(checked_state.get())


# Variable to hold on to checked state. 0 is Off, 1 is On
checked_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
check_button.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# variable to hold on to which calculate_button value is checked
radio_state = IntVar()
radiobutton_1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton_2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton_1.pack()
radiobutton_2.pack()


# Listbox
def listbox_used():
    """gets current selection from listbox"""
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Banana", "Orange"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()
