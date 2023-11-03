import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, )
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="25:00")
    global reps
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    print(reps)
    if reps > 8:
        pass
    if reps % 8 == 0:
        print("long break min")
        title_label.config(text="Break", fg=RED)
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 0:
        print("short break min")
        title_label.config(text="Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
    else:
        print("work min")
        title_label.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # pre chatgpt time format
    # print(count)
    # canvas.itemconfig(timer_text, text=count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        global reps
        marks = ""
        work_sessions = math.floor(reps / 2)
        print(reps)
        print(work_sessions)
        for _ in range(work_sessions):
            marks += '✅'
        check_marks.config(text=marks)

        start_time()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="25:00", fill="black", font=(FONT_NAME, "35", "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, bd=0, command=start_time)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, bd=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

# keep the window open
window.mainloop()
