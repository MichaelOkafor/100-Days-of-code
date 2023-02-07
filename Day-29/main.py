from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
               "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+"]
    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = password_symbols + password_numbers + password_letters
    random.shuffle(password_list)

    # the code below is the same.
    # password = ""
    # for char in password_list:
    #     password += char
    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    # check if the password or email entry is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        # to use a message box
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}"
                                                              f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)  # the width & height is divided by 2 to place the image in the middle
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()  # this place the cursor on the website entry when the app is launched

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "michael@gmail.com")  # takes an index (either 0 or END and the string you want to insert)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
