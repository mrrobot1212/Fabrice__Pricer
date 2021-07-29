from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
from datetime import date 
from datetime import timedelta 
from dateutil.relativedelta import relativedelta




root=Tk()

results_ = []


def func3_365_():

    
    fields = ('Annual Rate, %', 'Loan Principle, $', 'Delay Start, (periods)', 'Annual Compounding Periods', 'Years Until Maturity', 'Total Payable, $', 'Maturity Date')

    
    

    def final_balance(entries):
        global results_

        today = date.today()
        maturity = today + relativedelta(days =+ int(365 * float(entries['Years Until Maturity'].get())))


        r = float(entries['Annual Rate, %'].get())
        loan = float(entries['Loan Principle, $'].get())
        delay_periods = float(entries['Delay Start, (periods)'].get())
        n =  float(entries['Annual Compounding Periods'].get())
        y = float(entries['Years Until Maturity'].get())
        payable = float(entries['Total Payable, $'].get())

        ###delay-calc###
        if delay_periods >= 0:
            x = ((loan * (1 + (r / 100))) - loan) * delay_periods
        else:
            print("Invalid entry")
            entries['Delay Start, (periods)'].delete(0, tk.END)
            entries['Delay Start, (periods)'].insert(0, tk.END)
        ###calc###
        fin = int(loan * (1 + (r/(n*100)))**(n*y)) 
        fin = int(fin + x) 
        fin = (f"{fin:,d}")
        entries['Total Payable, $'].delete(0, tk.END)
        entries['Total Payable, $'].insert(0, fin )
        entries['Maturity Date'].delete(0, tk.END)
        entries['Maturity Date'].insert(0, maturity.strftime("%b %d %Y"))
        results_.append(fin)
        print(results_)



        
    def make_form(root, fields):
            
        entries={}
        for field in fields:
            print(field)
            row = tk.Frame(root)
            lab = tk.Label(row, width=22, text=field + ": ", anchor='w')
            ent = tk.Entry(row)
            ent.insert(0, "0")
            row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
            lab.pack(side=tk.LEFT)
            ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
            entries[field] = ent
        return entries 

  


    def start3_365_():
        
        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Delayed Compund Interest - 365")
            ents = make_form(root, fields)
            s2 = 'style2.TButton'
            s = ttk.Style()
            s.map(s2, foreground=[('', 'blue')])
            b1 = ttk.Button(root, style=s2, text='Amount Payable', command=(lambda e=ents: final_balance(e)))
            b1.pack(side=tk.LEFT, padx=5, pady=5)
            b2 = ttk.Button(root, style=s2, text='Quit', command=root.destroy)
            b2.pack(side=tk.LEFT, padx=5, pady=5)
            
           

    style2 = ttk.Style()
    style2.configure('TEntry', foreground='blue')
    start3_365_()
#---Func3End---#






















#------ResultsWindow------#
def results():

    global results_

    root = tk.Tk()
    root.title("Results")
    root.geometry("550x300")
    menubar = Menu(root)
    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='Total of All Results', command=None)#(results__t)#
    file.add_command(label='New', command=None)
    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=help)
    help.add_command(label='Call Dimitri', command=None)
    root.config(menu=menubar)
    
    lbl = Label(root, text='To see options, click File.')
    lbl.grid(column=0, row=200)
    lbl.place(x=265, y=35, anchor="center")
    
    

    def _sum(results_):
        

        sum=0

        for i in results_ :
            sum = sum + float(i)
        return (sum)

    ans = _sum(results_)
    print("Total of all funtions is, " , ans)
    lbl_txt = Label(root, text="Total Payable from all functions is: ")
    lbl_txt.grid(column=0, row=200)
    lbl_txt.place(x= 265, y=65, anchor="center")
    lbl_ans = Label(root, text=ans)
    lbl_ans.grid(column=0, row=200)
    lbl_ans.place(x=265, y=100, anchor="center")


   

    
    root.mainloop()
#--options window--#

def opt_win():

        
    root.title("Option Select")
    root.geometry('550x300')
    menubar = Menu(root)

    file = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='File', menu=file)
    file.add_command(label='func3 365 fix', command=func3_365_)
    file.add_command(label='Results', command=results)
    file.add_command(label='Quit', command=root.destroy)


    help = Menu(menubar, tearoff=0)
    menubar.add_cascade(label='Help', menu=help)
    help.add_command(label='Call Dimitri', command=None)
    root.config(menu=menubar)

    lbl = Label(root, text="To see option, click File.")
    lbl.grid(column=0, row=200)
    lbl.place(x=265, y=35, anchor="center")

    lbl2 = Label(root, text="")
    lbl2.grid(column=0, row=200)
    lbl2.place(x=265, y=10, anchor="center")

    root.mainloop()
###---end---###

opt_win()