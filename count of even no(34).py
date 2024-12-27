Num=int(input("enter the integer:"))
Even_number_count=0
for i in range(1,Num+1):
    if(i%2==0):
        Even_number_count=Even_number_count+1
print("count of even numbers from 1 to ",Num,":",Even_number_count)