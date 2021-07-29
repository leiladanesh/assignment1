#name= (input("enter your name:")
#family= (input("enter your family:"))
n=input('enter your name:')
f=input('enter your name:')

s1=float(input('enter score first:'))
s2=float(input('enter score second:'))
s3=float(input('enter score third:'))

sum=s1+s2+s3
avg=sum/3

if avg >= 17 :
    print(n,f,'average=',avg,"your condition is grat")
elif avg < 17 and avg >=12:
    print (n,f,'average=',avg,"your condition is normal") 
elif avg <12:
    print(n,f,'average=',avg,"your condition is fail")







