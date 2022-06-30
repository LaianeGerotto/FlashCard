
from tkinter import *
import pandas
import random

BG_COLOR = "#B1DDC6"
cartao_atual = {}
to_learn = {}

try:
  data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  original = pandas.read_csv("data/words.csv")
  to_learn = original.to_dict(orient="records")
else:
  to_learn = data.to_dict(orient="records") #transforma os dados em dicionários - "orient, coloca a palavra PT e EN no mesmo dict"



def next_card():
  global cartao_atual, flip_timer
  window.after_cancel(flip_timer)
  cartao_atual = random.choice(to_learn)
  canvas.itemconfig(card_title,text="Português",fill="black")
  canvas.itemconfig(card_word, text=cartao_atual["Portugues"],fill="black")
  canvas.itemconfig(card_background, image=card_front_img)
  flip_timer = window.after(3000, func=flip_card)


def flip_card():
  canvas.itemconfig(card_title,text="English", fill="white")
  canvas.itemconfig(card_word, text=cartao_atual["English"],fill="white")
  canvas.itemconfig(card_background, image=card_back_img)


def is_known():
  to_learn.remove(cartao_atual)
  data = pandas.DataFrame(to_learn)
  data.to_csv("data/words_to_learn.csv", index=False)
  next_card()

window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BG_COLOR)
flip_timer = window.after(1000, func=flip_card)

#Importação da imagem e formatação dos textos
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="imagens/card_front.png")
card_back_img = PhotoImage(file="imagens/card_back.png")
card_background = canvas.create_image(400,263, image=card_front_img)
card_title = canvas.create_text(400,150,text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400,263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BG_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

#Criação os botões
wrong_image = PhotoImage(file="imagens/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="imagens/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()
window.mainloop()


