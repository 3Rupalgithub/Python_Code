#Python program for calculator
def add(num1,num2):
    return num1 + num2
def subtract(num1,num2):
    return num1- num2
def multiply(num1,num2):
    return num1* num2
def divide(num1,num2):
    return num1 / num2
num1 = int(input ('Enter a num1:'))
num2 = int(input('Enter a num2:'))
opr = int(input('Enter 1. Addition, 2. Subtraction, 3.Multiply, 4. Divide'))
if opr == 1:
    a=add (num1,num2)
    print(a)
elif opr == 2:
    a=subtract(num1,num2)
    print(a)
elif opr == 3:
    a=multiply(num1,num2)
    print(a) 
elif opr == 4:
    a=divide(num1,num2)
    print(a)
else : print("invalid operator")
    
