import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog

win = Tk()
win.geometry("750x150")

def open_files():
    path = filedialog.askopenfilename(title="Select a file", filetypes=(("all files", "*.*")))

    file = open(path, 'r')
    txt = file.read()
    label.config(text = txt, font=('Courier 13 bold'))
    file.close()
    button.config(state=DISABLED)
    win.geometry("750x450")

label = Label(win, text="", font=('Courier 13 bold'))
label.pack()

button = ttk.Button(win, text="Open", command=open_files)
button.pack(pady=30)
win.mainloop()
#search through file locations designated
#catalog what's in each folder
#folder name, file name, file size, last modified, size
#when program starts have button to press to choose folder
#defaults to current folder application is in
