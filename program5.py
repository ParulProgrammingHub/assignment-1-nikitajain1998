#program 5
#wpp to enter value in days and convert in form of years,months and days
days=int(input("enter the number of days"))
year=int(days/360)
r=int(days%360)
m=int(r/30)
d=int(r%30)
print(" %d year %d month %d days" %(year,m,d))
