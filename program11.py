#program 11
#wpp to enter principal amount,time and interest rate.create
#compound_interest(principal,time,rate)function to calculate compound interest. 

pa=float(input("enter the principal amount"))
time=float(input("enter the time period"))
interestrate=float(input("enter the interest rates"))
n=float(input("number of time per year rate is compounded"))
ir=interestrate/100
a=1+ir/n
b=n*time
def compound_interest(pa,time,ir):
    ta=pa*a**b
    print("total amount(principal + interest) = %f "%(ta))
compound_interest(pa,time,ir)

