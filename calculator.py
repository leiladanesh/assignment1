import math

op=input('enter operator:')
if op=='sin' or  op=="cos" or op=='sqrt' or op=='tan' or op=='cot'or  op=='fac' or op=='%':
    a=float(input("enter number:"))
else:    

    a = float(input('enter number1:'))
    b = float(input('enter number2:'))

if op=="+":
    result= a+b
elif   op=="-":
    result= a-b
elif op=="*":
    result= a*b
elif op== '/':
    if b==0:
        result='cannot divide by zero'
    else:
        result=a/b  
elif op=='%':
    result =a/100
elif op=="^":
    result=a**b                  

elif op=='log':
    result=math.log(a,b)
elif op=="sqrt":
    result = math.sqrt(a) 
elif op=='sin':
    c =(a / 180) * math.pi
    result = math.sin(c)
elif op=='cot':
    c =(a/180)*math.pi
    result = 1/math.tan(c)    
elif op=='cos':
    result = math.cos(a)
elif op=='tan':
    c =(a/180)*math.pi
    result = math.tan(c) 
elif op=='fac':
    result=math.factorial(a)       

print(result)     

