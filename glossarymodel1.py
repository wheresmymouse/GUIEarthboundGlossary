# import components for GUI design from tkinter

from tkinter import *

# main window is created
# window is given a title
# window background color is set to black

user_window = Tk()
user_window.title("Earthbound Glossary")
user_window.configure(background = "black")

# adjustments are made so that the program can expand and wrap to the window size

user_window.rowconfigure(0, weight = 1)
user_window.columnconfigure(0, weight = 1)

# labels give user instructions on how to use the entry bar

def_label = Label (user_window, text = "Enter the word you would like a definition for: ", bg = "black", fg = "white", font = "none 12 bold")
def_label.grid (row = 0, column = 0, sticky = W)
##def_label.pack()

# entry bar for glossary

textentry = Entry(user_window, width = 20, bg = "white")
textentry.grid (row = 0, column = 1, sticky = E)
##textentry.pack()

# label tells user where the definition will appear

return_label = Label(user_window, text = "Definition: ", bg = "black", fg = "white", font = "none 12 bold")
return_label.grid (row = 2, column = 0, sticky = W)

# photo is added to the bottom of the window

img = PhotoImage(file='eb1.png')
Label(
user_window,
image=img
).grid(row = 9, column = 0, sticky = S)

##return_label.pack()

##img = ImageTk.PhotoImage(Image.open("GIYGAS.gif"))
##imglabel = Label(image = img)
##img.grid (row = 9, column = 1, sticky = S)

##filename = "GIYGAS"
##im = Image.open(filename)
##im=ImageTk.PhotoImage(im)

##img=PhotoImage(file='GIYGAS.gif')
##Label(user_window,image=img).pack()
##
##s=Label(user_window,text="Img",image=im) 
##s.grid(row=0,column=0)

output = Text (user_window, width = 75, height = 6, wrap = WORD, background = "white")
output.grid(row = 3, column = 0, columnspan = 2, sticky = W)
##output.pack()

##image = Tkinter.PhotoImage(file="GIYGAS.gif")
##Tkinter.Label(root, image=image).grid(row = 0, column = 5, sticky = S)

##photo1 = PhotoImage(file = "GIYGAS.gif")
##Label(user_window, image = photo1, bg = black)
##photo1.grid(row = 0, column = 5, sticky = S)
##label.pack()

# submit function is arranged
# dictionary keys are entered

def submit():
    earthbound_dictionary = {
        'Giygas':'powerful being from another world',
        'Ness':'protagonist and first playable character, boy with psychic powers from Onett, uses baseball bats',
        'Paula':'girl with psychic powers from Twoson, uses frying pans and pray command'
    }

    entered_text = textentry.get()
    if len(entered_text) > 0:
        output.delete(1.0, END)
        output.insert(END, earthbound_dictionary[entered_text])
    else:
        output.insert(END, 'Invalid Dictionary Entry')

# submit button is placed, calls submit function on click

submit_button = Button (user_window, text = "SUBMIT", width = 0, command = lambda: submit())
submit_button.grid(row = 1, column = 0, sticky = W)
##submit_button.pack()
##user_window2 = Toplevel()


##def openNewWindow():
##     
##
##    user_window2 = Toplevel(user_window)
##    user_window2.title("Exit Program?")
##    user_window2.geometry("200x200")
##    exitLabel = Label(user_window2, text ="Are you sure you wish to exit?")
##    user_window2.grid (row = 1, column = 1, sticky = E)
##
##    exit_button = Button(master, text ="EXIT", command = open.user_window2)
##    exit_button.pack(pady = 10)



# a function is created for the EXIT button command
# a new window will appear to ask the user if they really want to exit
# new window has a label and two buttons, YES and NO
# YES button closes both windows
# NO button just closes the exit window

def EXITW():
    user_window2 = Toplevel(user_window)
    user_window2.title("Exit Glossary?")
    user_window2.geometry("300x300")
    user_window2.configure(background = "black")
    exit_label = Label (user_window2, text = "Are you sure you wish to leave?", bg = "black", fg = "white", font = "none 12 bold")
    exit_label.grid(row = 1, column = 0, sticky = N)
    yes_button = Button (user_window2, text = "YES", width = 0, command = lambda: close_window())
    yes_button.grid(row = 4, column = 0, sticky = W)
    no_button = Button (user_window2, text = "NO", width = 0, command = lambda: user_window2.destroy())
    no_button.grid(row = 4, column = 4, sticky = E)

    def close_window():
        user_window2.destroy()
        user_window.destroy()
        exit()

# exit button, calls upon exit command when clicked

exit_button = Button (user_window, text = "EXIT", width = 0, command = lambda: EXITW())
exit_button.grid(row = 1, column = 1, sticky = E)



user_window.mainloop()


