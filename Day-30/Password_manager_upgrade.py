from tkinter import *
from tkinter import messagebox
import random
import json


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

    password = "".join(password_list)

    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    # check if the password or email entry is empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you have not left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new one
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


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
website_input = Entry(width=21)
website_input.grid(column=1, row=1)
website_input.focus()  # this place the cursor on the website entry when the app is launched

email_input = Entry(width=37)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "michael@gmail.com")  # takes an index (either 0 or END and the string you want to insert)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Button
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)
window.mainloop()
