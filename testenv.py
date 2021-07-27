an_ra = 0
ra_unsp = 0 
amm_with = 0 
t_loan = 0 
delay_periods = 0
t_periods = 0 
monthly_p = 0
fin_pay = 0 

def logic_check():
    global an_ra
    global ra_unsp
    global amm_with
    global t_loan
    global delay_periods
    global t_periods
    global monthly_p
    global fin_pay

    
    def user_input():
        
        an_ra = float(input("Enter annual rate: "))
        ra_unsp = float(input("Enter rate for unspent: "))
        amm_with = float(input("enter amount withdrawn: "))
        t_loan = float(input("enter total loan: "))
        delay_periods = float(input("enter delay periods: "))
        t_periods = float(input("enter total periods: "))
        monthly_p = float(input("enter no of monthly payments: "))
        fin_pay= "amount payable"
        
    
    def first_calc():
        comp_pers = float(t_periods - delay_periods)
        print(comp_pers)
        


 

