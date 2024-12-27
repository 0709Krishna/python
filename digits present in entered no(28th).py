Num=int(input("enter the integer value:"))
DigitCount=0
#condition to get number of digits (Num=25)
while(Num!=0):
    Num=Num//10
    DigitCount=DigitCount+1
print(DigitCount,"Digits")