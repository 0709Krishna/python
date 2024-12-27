Num=int(input("enter the integer:"))
Odd_number_count=0
for i in range(1,Num+1):
    if(i%2!=0):
        Odd_number_count=Odd_number_count+1
print("count of odd numbers from 1 to ",Num,":",Odd_number_count)