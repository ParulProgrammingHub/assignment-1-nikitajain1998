#program 9
#wpp to enter marks of 5 subjects and find the mean of 5 subjects, calculate percentage.
#if percentage is less than 35 print fail else print pass

a=float(input("enter the marks of 1 subject"))
b=float(input("enter the marks of 2  subject"))
c=float(input("enter the marks of 3 subject"))
d=float(input("enter the marks of 4 subject"))
e=float(input("enter the marks of 5 subject"))
sum=a+b+c+d+e
mean=sum/5
print("mean of 5 subjects is %f " %(mean))
per=mean
if(per>35):
    print("pass")
else:
    print("fail")
