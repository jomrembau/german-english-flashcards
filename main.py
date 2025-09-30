from tkinter import *
import tkinter as tk
import random

win = tk.Tk()

done_list = []
word_dictionary = {}

def disable_buttons():
    for w in win.winfo_children():
        if w.winfo_class() == "Button":
            w.configure(state="disabled")

def enable_buttons():
    for w in win.winfo_children():
        if w.winfo_class() == "Button":
            w.configure(state="active")

def generate_words():
    global word_list
    with open('words.txt') as f:
        datafile = f.readlines()
        for line in datafile:
            part = line.split("|")
            german = part[0].strip()
            english = part[1].strip()
            word_dictionary[german] = english
            word_list = list(word_dictionary)

def random_word():
    language_label.config(text="German")
    random_choice = random.choice(word_list)
    if random_choice not in done_list:
        word_label.config(text = random_choice)
    else:
        random_choice()

def add_to_done():
    disable_buttons()
    done_list.append(word_label.cget("text"))
    display_english()

def display_english():
    language_label.config(text= "English")
    german_word = word_label.cget("text")
    english_word = word_dictionary[german_word]
    word_label.config(text = english_word)
    win.after(2000, enable_buttons)
    win.after(2000, random_word)

win.title("English - German Flashcards")
win.geometry("800x600")
win.config(bg="#FDF6E3")

check_photo = PhotoImage(file = r"check.png")
eks_photo = PhotoImage(file = r"eks.png")

smaller_check = check_photo.subsample(3, 3)
smaller_eks = eks_photo.subsample(3, 3)

language_label = Label(text="German", bg= "#FDF6E3",fg= "#2C3E50", font=("Arial", 35, "italic"))
language_label.pack(side="top", pady=70)

word_label = Label(text="", bg= "#FDF6E3",fg= "#88B04B", font=("Arial", 35, "italic"))
word_label.pack(side="top")

check_button = Button(image=smaller_check, bg="#FF6F61", command=add_to_done)
check_button.pack(side="right", anchor=SE, pady= 60,padx= 100)

eks_button = Button(image=smaller_eks, bg="#FF6F61", command=display_english)
eks_button.pack(side="left", anchor=SW, pady= 60, padx= 100)

generate_words()
random_word()

win.mainloop()
