num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
num3=int(input("enter the integer:"))
if(num1<num2) and (num1<num3):
    smallest=num1
elif(num2<num1) and (num2<num3):
    smallest=num2
else:
    smallest=num3
print(smallest,"is smallest number")