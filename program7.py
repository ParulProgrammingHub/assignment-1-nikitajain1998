#program 7
#wpp to enter 2 angles and using function thirdangle(angle1,angle2) calculate 3 angle

angle1=float(input("enter the value of first angle"))
angle2=float(input("enter the value of second angle"))
def thirdangle( angle1,angle2 ):
    su=angle1+angle2
    ans=180-su
    print("value of third angle is %f "%(ans))
thirdangle(angle1,angle2)
