from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
# colors from colorhunt.co
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 0
checks = ''
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    global checks
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    timer_label.config(text='Timer')
    checks = ''
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    global checks
    reps += 1
    if reps in [1, 3, 5, 7]:
        count_down(int(WORK_MIN * 60))
        timer_label.config(text='Work', fg=GREEN)
        check_label.config(text=f'{checks}')
    elif reps in [2, 4, 6]:
        count_down(int(SHORT_BREAK_MIN * 60))
        timer_label.config(text='Short Break', fg=PINK)
        checks = checks + '✓'
    elif reps == 8:
        count_down(int(LONG_BREAK_MIN * 60))
        timer_label.config(text='Long Break', fg=RED)
        reset_timer()
    print(checks, reps)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f'0{sec}'
    canvas.itemconfig(timer_text, text=f'{min}:{sec}')
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    if count == 0:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
# window
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)

# labels
dummy_label = Label(text='')
dummy_label.grid(column=0, row=0)
timer_label = Label(text='Timer', font=(FONT_NAME, 20, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(column=1, row=0)
check_label = Label(text=f'', font=(FONT_NAME, 15, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_label.grid(column=1, row=3)

# buttons
start_button = Button(text='START', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='RESET', command=reset_timer)
reset_button.grid(column=2, row=2)

# tomato image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text='0:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

window.mainloop()

# notes
# GUI is event driven--check if something happened every millisecond, not timed
# dynamic typing: change data type when store new data inside it
# strong: type does not change unintentionally
# dynamic: data holds type, not variable, so it can be changed

# how to access element in canvas: canvas.itemconfig()

# using timer function in GUI
# 1000 milliseconds = 1 sec
# def say_something(thing, other_thing):
#     print(thing)
# window.after(1000, say_something, 3, 'Hello')
