from tkinter import *
from random import choice
import pandas

# ------------- CONSTANTS
BACKGROUND_COLOR = "#B1DDC6"
new_word = {}
to_learn = {}

# ------------- FUNCTIONALITY
try:
    german_words_file = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pandas.read_csv("./data/german_words.csv")
    to_learn = original_file.to_dict(orient="records")
else:
    to_learn = german_words_file.to_dict(orient="records")


def is_known():
    global new_word
    to_learn.remove(new_word)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_random_word()


def new_random_word():
    global new_word, flip_timer
    window.after_cancel(flip_timer)
    new_word = choice(to_learn)
    canvas.itemconfig(title, text="Deutsch", fill="black")
    canvas.itemconfig(word, text=new_word["Deutsch"], fill="black")
    canvas.itemconfig(card_background, image=logo_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_background, image=logo_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=new_word["English"], fill="white")


# ------------- UI SETUP
# Window
window = Tk()
window.title("Flashcards Deutsch")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
logo_front = PhotoImage(file="./images/card_front.png")
logo_back = PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400, 263, image=logo_front)
title = canvas.create_text(400, 150, text="language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
wrong_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, pady=50, command=new_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, pady=50, command=is_known)
right_button.grid(row=1, column=1)

new_random_word()

window.mainloop()

