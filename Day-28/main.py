from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it is the 8th rep:  # remember the % returns the remainder after a clean division
    if reps % 8 == 0:
        count_down(long_break_sec)
        title.config(text="Break", foreground=RED)
    # if it is the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title.config(text="Break", foreground=PINK)
    else:
        # if it is the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title.config(text="Work", foreground=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)  # converts the number to a whole number
    count_sec = count % 60  # remember the % returns the remainder after the division.
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "-/"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)  # the width & height is divided by two to put the image in the center
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title = Label(text="Timer", foreground=GREEN, background=YELLOW, font=(FONT_NAME, 50))
title.grid(column=1, row=0)

start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(foreground=GREEN, background=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
