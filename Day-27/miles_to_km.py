from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=200, height=100)
window.config(pady=100, padx=100)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Label
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

kilometer_label = Label(text="km")
kilometer_label.grid(column=2, row=1)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

calculate_button = Button(text="calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
