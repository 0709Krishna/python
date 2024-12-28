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
N1=str(input("enter the first number:"))
N2=str(input("enter the second number:"))
print("before swapping:")
print("N1=",N1)
print("N2=",N2)
N1=N1+N2
N2=N1-N2
N1=N1-N2
print("after swapping:")
print("N1=",N1)
print("N2=",N2)
#swapping using third variable
Num5=int(input("enter the first number:"))
Num6=int(input("enter the second number:"))
print("before swapping:")
print("Num5=",Num5)
print("Num6=",Num6)
temp=Num5
Num5=Num6
Num6=temp
print("after swapping:")
print("Num5=",Num5)
print("Num6=",Num6)