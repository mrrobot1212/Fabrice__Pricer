
def total_payable():
    nominal = int(input("Enter principal amount: "))
    r = float(input("Enter the nominal interest rate (decimal): "))
    n = int(input("Enter number of compounding periods: "))
    t = float(input("Enter time in decimal years: "))

    x = n * t
    y = (1 + (r/n))
    A = pow(y,x)
    A = A * nominal
    A = round(A, 2)
    print("Total Amount owed is: ", A)

total_payable()



