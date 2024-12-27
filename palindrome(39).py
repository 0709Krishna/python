num=int(input("enter the integer:"))
rev=0
rem=0
temp=num
while(num!=0):
    rem=num%10
    rev=rev=rev*10+rem
    num=num//10
if(temp==rev):
    print(temp,"is palindrome")
else:
    print(temp,"is not palindrome")
   
    
