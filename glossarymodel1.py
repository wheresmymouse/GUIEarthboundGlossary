# import components for GUI design from tkinter

from tkinter import *

def submit():
    entered_text = textentry.get()

user_window = Tk()
user_window.title("Earthbound Glossary")
user_window.configure(background = "black")

photo1 = PhotoImage(file="GIYGAS.gif")
photo_label_1 = Label (user_window, image = photo1, bg = "black") .grid (row = 0, column = 0, sticky = W)

def_label = Label (user_window, text="Enter the word you would like a definition for: ", bg = "black", fg = "white", font = "none 12 bold") .grid (row = 1, column = 0, sticky = W)

textentry = Entry(user_window, width = 20, bg = "white")
textentry.grid (row = 2, column = 0, sticky = W)

submit_button = Button (user_window, text = "SUBMIT", width = 0, command = submit) .grid (row = 3, column = 0, sticky = W)

return_label = Label (user_window, text = "/nDefinition: ", bg = "black", fg = "white", font = "none 12 bold") .grid (row = 4, column = 0, sticky = W)

output = Text (user_window, width = 75, height = 6, wrap = WORD, background = "white")
output.grid (row = 5, column = 0, columnspan = 2, sticky = W)

earthbound_dictionary = {
    'Giygas':'powerful being from another world',
    'Ness':'protagonist and first playable character, boy with psychic powers from Onett, uses baseball bats',
    'Paula':'girl with psychic powers from Twoson, uses frying pans and pray command',
    }

user_window.mainloop()

