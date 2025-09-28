#celsius to fahrenheit
c=input('celsius : ')
c=float(c)
f=(c*9/5)+32
print('fahrenheit: ',f)
#fahrenheit to celsius
f=input("fahrenheit : ")
f=float(f)
c=(f-32)/1.8
print('celsius' ,c)
#simple interest calculator
#equation is pnr/100
p=input('principle : ')
p=int(p)
n=input('times (in years): ')
n=int(n)
r=input('rate : ')
r=int(r)
SI=(p*n*r)/100
print('Simple Interest is' , SI)