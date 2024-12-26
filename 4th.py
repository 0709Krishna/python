Num=int(input("enter the integer:"))
if(Num>=-9 and Num<=9):
    print("it is not two digit")
elif(Num>=-99 and Num<=99):
    print("it is a  two digit")
else:
    print("it is not  two digit number")
print("--------------------------------------------------")
Num=int(input("enter the integer:"))
if((Num>=10 and Num<=99) or (Num>=-99 and Num<=-10)):
    print("Two digit number")
else:
    print("Not a two digit number")
# user entered integer is a two digit number or not