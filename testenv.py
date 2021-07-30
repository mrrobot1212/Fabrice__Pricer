from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter as tk
import random


root=Tk()

results_ = []



#---Func4Start---#
def func4_365():

    fields = ('Annual Rate, %', 'Rate for Unspent, %',  'Amount Withdrawn, $', 'Total Loan, $', 'Delay Start, (periods)', 'Number of Periods', 'No. of Monthly Payments',  'Amount Payable, $')

    def monthly_payment(entries):

        r = float(entries['Annual Rate, %'].get()) / 100 / 12
        total_withdrawn = float(entries['Amount Withdrawn, $'].get())
        total_periods = float(entries['Number of Periods'].get())
        delay_periods = float(entries['Delay Start, (periods)'].get())
        remaining_loan = float(entries['Amount Payable, $'].get())
        #calc#
        comp_periods = float(total_periods - delay_periods) #n0 of compounding periods
        q = (1 + r) ** delay_periods #percentage ^compounding periods
        x = total_withdrawn * (1 + r) - total_withdrawn
        q = (1 + r) ** comp_periods
        monthly = r * ( (q * total_withdrawn - remaining_loan) / ( q - 1 ))
        monthly = ("%8.2f" % monthly).strip()
        entries['No. of Monthly Payments'].delete(0, tk.END)
        entries['No. of Monthly Payments'].insert(0, monthly )
        print("Monthly Payment: %f" % float(monthly))

        
    def final_balance(entries):
                         
        r = float(entries['Annual Rate, %'].get()) / 100 / 12
        u = float(entries['Rate for Unspent, %'].get()) / 100 / 12
        total_withdrawn = float(entries['Amount Withdrawn, $'].get())
        total_loan = float(entries['Total Loan, $'].get())
        total_periods = float(entries['Number of Periods'].get())
        delay_periods = float(entries['Delay Start, (periods)'].get())
        monthly = float(entries['No. of Monthly Payments'].get())
        remaining_loan = float(entries['Amount Payable, $'].get())
        comp_periods = float(total_periods - delay_periods)
        #calculation#
        x = total_withdrawn * (1 + r) - total_withdrawn
        if comp_periods > 1: 
            x  = (total_withdrawn * (1 + r) - total_withdrawn) * delay_periods
        q = (1 + r) ** comp_periods
        unspent = total_loan - total_withdrawn
        unspent_r = (unspent * ((1 + u) ** total_periods)) - (unspent)
        monthly = r * ( (q * total_withdrawn - remaining_loan) / ( q - 1 ))
        remaining = (q * total_withdrawn - ((q - 1) / r) * monthly) + (unspent_r)
        monthly = ("%8.2f" % monthly).strip()
        remaining = remaining + x
        remaining = ("%8.2f" % remaining).strip()
        print(x)
        entries['Amount Payable, $'].delete(0, tk.END)
        entries['Amount Payable, $'].insert(0, remaining)
        print("Amount Payable: %f" % float(remaining))


    def makeform(root, fields):

        entries = {}
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
    
    
    def start4_365():

        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Delay + (Un)-Used Funds Interst Calc - 365")
            ents = makeform(root, fields)
            s2 = 'style2.TButton'
            s = ttk.Style()
            s.map(s2, foreground=[('', 'blue')])
            b1 = ttk.Button(root, style=s2, text='Final Balance', command=(lambda e=ents: final_balance(e)))
            b1.pack(side=tk.LEFT, padx=5, pady=5)
            b3 = ttk.Button(root, style=s2, text='Quit', command=root.destroy)
            b3.pack(side=tk.LEFT, padx=5, pady=5)

    style2 = ttk.Style()
    style2.configure('TEntry', foreground='blue')
    start4_365()




def func4_360():

    fields = ('Annual Rate, %', 'Rate for Unspent, %',  'Amount Withdrawn, $', 'Total Loan, $', 'Delay Start, (periods)', 'Number of Periods', 'No. of Monthly Payments',  'Amount Payable, $')

    def monthly_payment(entries):

        r = float(entries['Annual Rate, %']).get() / 100 / 360
        r= r * 30.41666667 * 1.013888889
        total_withdrawn = float(entries['Amount Withdrawn, $']).get()
        total_periods = float(entries['Number of Periods']).get()
        delay_periods = float(entries['Delay Start, (periods)']).get()
        remaining_loan = float(entries['Amount Payable, $']).get()
        #calc#
        comp_periods = float(total_periods - delay_periods)
        q = (1 + r)** delay_periods
        x = total_withdrawn * (1 + r) - total_withdrawn
        if comp_periods > 1: 
            x  = (total_withdrawn * (1 + r) - total_withdrawn) * delay_periods
        q = (1 + r) ** comp_periods
        monthly = r * ( (q * total_withdrawn - remaining_loan) / ( q - 1 ))
        monthly = ("%8.2f" % monthly).strip()
        entries['No. of Monthly Payments'].delete(0, tk.END)
        entries['No. of Monthly Payments'].insert(0, monthly )
        print("Monthly Payment: %f" % float(monthly))

        
    def final_balance(entries):
        
        r = (float(entries['Annual Rate, %'].get())) / 100 / 360
        r = r * 30.41666667 * 1.013888889
        u = (float(entries['Rate for Unspent, %'].get())) / 100 / 360
        total_withdrawn = float(entries['Amount Withdrawn, $'].get())
        total_loan = float(entries['Total Loan, $'].get())
        total_periods = float(entries['Number of Periods'].get())
        delay_periods = float(entries['Delay Start, (periods)'].get())
        monthly = float(entries['No. of Monthly Payments'].get())
        remaining_loan = float(entries['Amount Payable, $'].get())
        comp_periods = float(total_periods - delay_periods)
        #calculation#
        x = total_withdrawn * (1 + r) - total_withdrawn
        if comp_periods > 1: 
            x  = (total_withdrawn * (1 + r) - total_withdrawn) * delay_periods
        q = (1 + r) ** comp_periods
        unspent = float(total_loan - total_withdrawn)
        unspent_r = (unspent * (1 + u) ** total_periods) - (unspent)
        monthly = r * ( (q * total_withdrawn - remaining_loan) / ( q - 1 ))
        remaining = (q * total_withdrawn - ((q - 1) / r) * monthly) + (unspent_r)
        monthly = ("%8.2f" % monthly).strip()
        remaining = remaining + x
        remaining = ("%8.2f" % remaining).strip()
        entries['Amount Payable, $'].delete(0, tk.END)
        entries['Amount Payable, $'].insert(0, remaining)
        print("Amount Payable: %f" % float(remaining))


    def makeform(root, fields):

        entries = {}
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
    
    
    def start4_360():

        if __name__ == '__main__':
            root = tk.Tk()
            root.title("Delay + (Un)-Used Funds Interst Calc - 360")
            ents = makeform(root, fields)
            s2 = 'style2.TButton'
            s = ttk.Style()
            s.map(s2, foreground=[('', 'blue')])
            b1 = ttk.Button(root, style=s2, text='Final Balance', command=(lambda e=ents: final_balance(e)))
            b1.pack(side=tk.LEFT, padx=5, pady=5)
            b3 = ttk.Button(root, style=s2, text='Quit', command=root.destroy)
            b3.pack(side=tk.LEFT, padx=5, pady=5)

    style2 = ttk.Style()
    style2.configure('TEntry', foreground='blue')
    start4_360()
#---Func4End---#










 

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
    file.add_command(label='Func4_360', command=func4_360)
    file.add_command(label='Func4_365', command=func4_365)
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

