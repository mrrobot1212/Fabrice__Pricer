import sys
import os
from tkinter import *
from tkinter.ttk import *
import main

root=Tk()

root.title("Option Select")
root.geometry('550x300')

#def run_main():
 #   os.system('python main.py')

menubar = Menu(root)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=file)
file.add_command(label='Interest Over Fixed Period', command=main)
file.add_command(label='new', command=None)
file.add_command(label='new', command=None)
file.add_command(label='Quit', command=root.destroy)

help = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Help', menu=help)
help.add_command(label='Call Dimitri', command=None)
root.config(menu=menubar)

lbl = Label(root, text="To see options, click File.")
lbl.grid(column=0, row=200)
lbl.place(x=245, y=35, anchor="center")
root.mainloop()


