import math
gh= int(input("please input height = "))
w = int(input(" please input weight "))
ghad = (gh/100)**2
bmi = w/ghad

if 25<= bmi < 30 :      
    print("fat")
elif  18<= bmi <25 :
    print("normal")
elif 18> bmi:
    print("skini")
elif 30<= bmi <40:
    print('very fat')   