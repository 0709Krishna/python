Num=int(input("Enter the integer value:"))
count=0
for i in range(1,Num+1):
    if(Num%i==0):
        count+=1
if(count==2):
    print("prime number")
else:
    print("not a prime number")
print("--------------------------------------------------------")
#Another way
for i in range(2,Num):
    if(Num%i==0):
        print("Not a prime number")
        break
else:
     print("prime number")
    