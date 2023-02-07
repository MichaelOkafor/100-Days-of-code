from tkinter import *


def button_clicked():
    new_text = Input.get()
    my_label.config(text=new_text)
    print("i got clicked")


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Labels
my_label = Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="new calculate_button", command=button_clicked)
new_button.grid(column=2, row=0)
# Entries
Input = Entry(width=30)
print(Input.get())
Input.grid(column=3, row=2)

window.mainloop()
