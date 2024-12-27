Num1=int(input("enter the first number:"))# swapping without using third variable
Num2=int(input("enter the second number:"))
print("before swapping:")
print("Num1=",Num1)
print("Num2=",Num2)
Num1,Num2=Num2,Num1
print("after swapping:")
print("Num1=",Num1)
print("Num2=",Num2)
print("------------------------------------------------------------------")
#swapping using arthimetic operators
Num1=str(input("enter the first number:"))
Num2=str(input("enter the second number:"))
print("before swapping:")
print("Num1=",Num1)
print("Num2=",Num2)
Num1=Num1+Num2
Num2=Num1-Num2
Num1=Num1-Num2
print("after swapping:")
print("Num1=",Num1)
print("Num2=",Num2)
#swapping using third variable
Num1=int(input("enter the first number:"))
Num2=int(input("enter the second number:"))
print("before swapping:")
print("Num1=",Num1)
print("Num2=",Num2)
temp=Num1
Num1=Num2
Num2=temp
print("after swapping:")
print("Num1=",Num1)
print("Num2=",Num2)