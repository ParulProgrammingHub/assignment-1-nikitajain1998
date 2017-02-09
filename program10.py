#program 10
#wpp to enter principal amount,time and interest rate.create
#simple_interest(principal,time,rate)function to calculate simple interest.

pa=float(input("enter the principal amount"))
time=float(input("enter the time period"))
interestrate=float(input("enter the interest rates"))
ir=interestrate/100

def simple_interest(pa,time,ir):
    interest=pa*time*ir
    ta = pa+interest
    print("total amount(principal+interest)=%f" %(ta))
simple_interest(pa,time,ir)
