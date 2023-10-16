# flashcard app for learning spanish words

from tkinter import *
from tkinter import messagebox
import pandas as pd
import random

# -------------------- INPUTS / CONSTANTS
# colors from colorhunt.co
BACKGROUND_COLOR = "#B1DDC6"
GREEN = '#698269'
BROWN = '#B99B6B'
TAN = '#F1DBBF'
RED = '#AA5656'
LARGE_FONT = ('ahoroni', 60, 'bold')
SMALL_FONT = ('arial nova', 20)
data_file = 'spanish_data.xlsx'
memory_file = 'spanish_data_memory.csv'
correct_english = []
incorrect_english = []
incorrect_spanish = []
num_correct = 0
num_incorrect = 0
word = 'Click "Start" to Begin'
spanish_word = ''
data = pd.DataFrame({
    'spanish': [],
    'english': []
})
timer = None

# -------------------- FUNCTIONS


def new_word():
    global word, data, timer
    start_button.config(text='Reset')
    word = random.choice(data.english)
    word_label.config(text=word)
    timer = window.after(5000, flip_card)


def data_select():
    global data
    cont = messagebox.askyesno(title='MEMORY', message='Continue where you left off?')
    if cont:
        try:
            data = pd.read_csv(memory_file)
        except FileNotFoundError:
            # read the full list
            data = pd.read_excel(data_file)
            # create a new memory .csv
            english_data = data.english.to_list()
            spanish_data = data.spanish.to_list()
            tmp_data = {
                'spanish': spanish_data,
                'english': english_data
            }
            df = pd.DataFrame(tmp_data)
            df.to_csv('spanish_data_memory.csv')
    else:
        data = pd.read_excel(data_file)


def reset():
    global word, incorrect_english, incorrect_spanish, num_incorrect, num_correct, data, timer
    data_select()
    start_button.config(text='Start')
    incorrect_english = []
    incorrect_spanish = []
    num_correct = 0
    num_incorrect = 0
    word = 'Click "Start" to Begin'
    new_word()


def flip_card():
    global spanish_word, data
    for r in range(0, len(data.english)):
        if data.english[r] == word:
            spanish_word = data.spanish[r]
    word_label.config(text=spanish_word)


def right_answer():
    global correct_english, correct_spanish, num_correct, word
    num_correct += 1
    correct_english = []
    correct_english.append(word)
    new_word()


def wrong_answer():
    global incorrect_english, incorrect_spanish, num_incorrect, word, spanish_word
    num_incorrect += 1
    incorrect_english.append(word)
    incorrect_spanish.append(spanish_word)
    new_word()


def stop_study():
    global data, timer
    window.after_cancel(timer)
    # create study guide of incorrect answers
    study_data = {'spanish': incorrect_spanish,
                  'english': incorrect_english}
    df = pd.DataFrame(study_data)
    df.to_csv('study_sheet.csv')
    word_label.config(text=f'Nice work!\nCorrect: {num_correct}\nIncorrect: {num_incorrect}'
                           f'\n\nCreated Study Sheet\nSee you next time!')
    # create memory file to pick up where we left off
    data_english = data.english.to_list()
    data_spanish = data.spanish.to_list()
    english_continue = []
    spanish_continue = []
    for w in range(0,len(data_english)):
        if data_english[w] not in correct_english:
            english_continue.append(data_english[w])
            spanish_continue.append(data_spanish[w])
    cont_data = {
        'spanish': spanish_continue,
        'english': english_continue}
    df_cont = pd.DataFrame(cont_data)
    df_cont.to_csv(memory_file)
    window.after_cancel(timer)


# -------------------- GUI
# window
window = Tk()
window.title('Flashy')
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

# canvas
canvas = Canvas(width=1400, height=750, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=1, row=0)
# titles
big_title = canvas.create_text(700, 50, text='Flashy!', fill=RED, font=LARGE_FONT)
small_title = canvas.create_text(700, 110, text='Spanish Edition', fill=RED, font=SMALL_FONT)
# right-wrong
check_image = PhotoImage(file=r'images\right.png')
x_image = PhotoImage(file=r'images\wrong.png')
# card
card_image = PhotoImage(file=r'images\card_front.png')
canvas.create_image(700, 400, image=card_image)

# buttons
# right-wrong
correct_button = Button(window, image=check_image, borderwidth=0, command=right_answer, highlightthickness=0)
correct_button.grid(column=0, row=2)
incorrect_button = Button(window, image=x_image, borderwidth=0, command=wrong_answer, highlightthickness=0)
incorrect_button.grid(column=2, row=2)
# start
start_button = Button(text='Start', font=SMALL_FONT, fg=RED, bg=TAN, command=reset, width=25, height=2)
start_button.grid(column=1, row=2)
# stop and study button
stop_button = Button(text='Stop & Study', font=SMALL_FONT, fg=RED, bg=TAN, command=stop_study, width=25, height=2)
stop_button.grid(column=1, row=1)

# labels
# word
word_label = Label(text=word, font=SMALL_FONT, fg=RED, bg='white', highlightthickness=0)
word_label.grid(column=1, row=0)

window.mainloop()
