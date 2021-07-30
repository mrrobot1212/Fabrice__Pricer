
from tkinter import *
from tkinter import messagebox

class MenuBar(Menu):
    def __init__(self, ws):
        Menu.__init__(self, ws)

        file = Menu(self, tearoff=False)
        file.add_command(label="New")     
        file.add_separator()
        file.add_command(label="Exit", underline=1, command=self.quit)
        self.add_cascade(label="File",underline=0, menu=file)

        view = Menu(self, tearoff=0)
        ratio = Menu(self, tearoff=0)
        for aspected_ratio in ('4:3', '16:9'):
            ratio.add_command(label=aspected_ratio)
        view.add_cascade(label='Ratio', menu=ratio)
        self.add_cascade(label='View', menu=view)




class MenuDemo(Tk):
    def __init__(self):
        Tk.__init__(self)
        menubar = MenuBar(self)
        self.config(menu=menubar)

if __name__ == "__main__":
    ws=MenuDemo()
    ws.title('Python Guides')
    ws.geometry('300x200')
    ws.mainloop()