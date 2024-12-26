Num=int(input("enter the value of Num:"))
print("Even numbers from 1 to",Num,":")
for i in range(1,Num+1):
    if(i%2==0):
        print(i)
# another way using step size
Num=int(input("enter the value of Num:"))
print("Even numbers from 1 to",Num,":")
for i in range(2,Num+1,2):
    print(i)

