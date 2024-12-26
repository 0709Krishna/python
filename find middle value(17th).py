num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
num3=int(input("enter the integer:"))
if(num1>num2 and num1<num3) or  (num1>num3 and num1<num2):
    print(num1," is middle number")
elif(num2>num1 and num2<num3) or (num2>num3 and num2<num1):
    print(num2," is middle number")
else:
    print("num3,is middle number")
