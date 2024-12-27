num=int(input("Enter the integer value:"))
temp=num
rev=0
rem=0
for i in range(2,num):
    if(num%i==0):
        print(num,"is not a palindrome")
        break
else:
    while(num!=0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if(temp==rev):
        print(temp,"is prime palindrome")
    else:
        print(temp,"is not a prime palindrome")

    