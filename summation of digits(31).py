Num=int(input("enter the integer:"))
sum_of_digits=0
while(Num!=0):
  rem=Num%10
  sum_of_digits=sum_of_digits+rem
  Num=Num//10
print("summation of digits are",sum_of_digits)
