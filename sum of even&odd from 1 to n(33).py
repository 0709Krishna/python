Num=int(input("enter the integer:"))
Evensum=0
Oddsum=0
for i in range(1,Num+1):
    if(i%2==0):
        Evensum=Evensum+i
    else:
        Oddsum=Oddsum+i
print("Even sum:",Evensum)
print("Odd sum:",Oddsum)