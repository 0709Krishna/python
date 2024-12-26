num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
num=max(num1,num2)
print(num)
print("------------------------------------------------")
num1=int(input("enter the integer:"))
num2=int(input("enter the integer:"))
if(num1>num2):
    print("num1 is greatest")
else:
    print("num2 is greatest")
print("--------------------------------------------")
#using ternary operator
result="num1 is greatest" if(num1>num2) else "num2 is greatest"
print(result)

    