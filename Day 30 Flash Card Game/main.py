from tkinter import *
import pandas as pd
from random import choice

try:
    esp_words = pd.read_csv("./data preprocessing/words_to_learn.csv")
except FileNotFoundError:
    esp_words = pd.read_csv("./data preprocessing/esp_word_list.csv")
    esp_words.to_csv("./data preprocessing/words_to_learn.csv")

esp_words_dict = esp_words.to_dict(orient="records")
random_choice = {}

# FLIP CARD FUNCTION
def flip_card():
    global random_choice
    canvas.itemconfig(card_bg,image=card_back)
    canvas.itemconfig(lang, text="English",fill="white")
    canvas.itemconfig(word, text=random_choice['English'],fill="white")

# NEW WORD GENERATOR
def gen_word():
    global random_choice, flip_timer
    window.after_cancel(flip_timer)
    random_choice = choice(esp_words_dict)
    canvas.itemconfig(lang,text="Spanish",fill="black")
    canvas.itemconfig(word,text=random_choice['Spanish'],fill="black")
    canvas.itemconfig(card_bg, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

# KNOW AND DONT_KNOW FUNCTIONS
def know():
    global random_choice
    esp_words_dict.remove(random_choice)
    words_to_learn = pd.DataFrame(esp_words_dict)
    words_to_learn.to_csv("./data preprocessing/words_to_learn.csv", index=False)
    gen_word()

def dont_know():
    gen_word()

# UI SETUP
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Spanish Flash Cards")

flip_timer = window.after(2000,func=flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./Images/card_front.png")
card_bg = canvas.create_image(400,263,image=card_front)
canvas.grid(row=0,column=0,columnspan=2)

card_back = PhotoImage(file="./Images/card_back.png")

lang = canvas.create_text(400,150,text="Language",fill="black",font=("Ariel",20,"italic"))
word = canvas.create_text(400,263,text="Word",fill="black",font=("Ariel",35,"bold"))

tick = PhotoImage(file="./Images/right.png")
tick_button = Button(image=tick,highlightthickness=0,command=know)
tick_button.grid(row=1,column=1)

cross = PhotoImage(file="./Images/wrong.png")
cross_button = Button(image=cross,highlightthickness=0,command=dont_know)
cross_button.grid(row=1,column=0)
gen_word()

window.mainloop()

wtl = pd.DataFrame(esp_words_dict)
wtl.to_csv("./data preprocessing/words_to_learn.csv",index=False)