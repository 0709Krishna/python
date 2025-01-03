def Display():
    print('python')
    print('java')
    print('c')
Display()
Display()
# multiple funcitons
def servefood():
    print("serve food")    
def eat():
    print("eat food")
def washhands():
    print("wash your hands")
    servefood()
    eat()
    print("wash your hands")
washhands()
servefood()
eat()
# variable shadowing concept-->local variable dominates global variable
# Global variable
Num=25
def value():
    Num=35  # Local variable
    print(Num)
value()
#  Return statement
def Display():
    return "Happy Morning..!"
Result=Display()
print(Result)
# Another example
def add(y):
    x=10
    c=x+y
    return c
sum=add(20)
print(sum)
# Nested  function
def disp():
    def show():
        print("show functon")
    print("Disp function")
    show()
disp()
# Example for parameterized function
def Add(a,b):
    return  a+b
def Sub(a,b):
    return a-b
def Mul(a,b):
    return a*b
def Div(a,b):
    return a//b
sum=Add(13,15)
print(sum)
Diff=Sub(45,87)
print(Diff)
Product=Mul(34,3)
print(Product)
quotient=Div(45,2)
print(quotient)
# Q) 
def print_table(n):
    for i in range(1,11):
        print(n,"x",i,"=",(n*i))
    print("-----------------------------------------------------")
# Function call
print_table(5)
print_table(7)
# Multiplication table from 1 to N
def mul_tables(n):
    for i in range(1,n+1):
      for j in range(1,11):
         print(i ,"x", j, "=",(i*j))
n=int(input("enter the value:"))
mul_tables(n)
# Nested function
def Display(n):
    print("I' m the function one")
    n()
def one():
    print("I' m first nested function")
def two():
    print("I' m second nested function")
Display(one)
Display(two)
# Actual arguments-->positional arguments
def priya(x, y):
    z=x**y
    print(z)
priya(5, 2)
#keyword arguments
def show(name,age):
     print(name,age)
show(name="kumar",age=62)
print()
# Default arguments
def show(name,age=27):
    print(name,age)
show(name="ram",age=62)
print()
# Variable length arguments
def add(*num):
    z=num[0]+num[1]+num[2]
    print(z)
add(5,6,2)
print()
# Lambda Function
Result=lambda Num:print(Num)
Result(100)
print()
Result1=lambda a,b:print(a**b)
Result1(3,2)
print()
# Returning multiple values using lambda function
add_sub=lambda x,y:(x+y,x-y)
a,s=add_sub(5,2)
print(a)
print(s)
print()
# Q) user enter is even or not using lambda function
Even_Odd=lambda Num:print("Even") if (Num%2==0) else print("Not even")
Even_Odd(45)
print()
# Q) integer digit or number using lambda
Even_Odd=lambda Num:print("Digit") if (Num>=-9 and Num<=9) else print("Number")
Even_Odd(5)
print()
# Q) user enter 2 digit or not
two_digit=lambda a:print("Two Digit") if((a>=10 and a<=99) or (a>=-99 and a<=-10)) else print("Not two digit")
two_digit(55)
# Q) integer palindrome or not using lambda
4

# Simple interest using lambda
Amount=int(input("Enter the Amount:"))
Interest=int(input("Enter the Rate of interest:"))
Time=int(input("Enter time in months:"))
Result=lambda Amount,Interest,Time:print((Amount*Interest*Time)/100)
Result(Amount,Interest,Time)
# Print no from 1 to n using lambda
Num=int(input("Enter the value of Num:"))
Res=list(map(lambda i:print(i),range(1,Num+1)))
# Print even no from 1 to n using lambda
N=int(input("Enter the value of Num:"))
list(map(lambda i:print(i),range(2,N+1,2)))
# Print odd no from 1 to n using lambda
N=int(input("Enter the value of Num:"))
list(map(lambda i:print(i),range(1,N+1,2)))
