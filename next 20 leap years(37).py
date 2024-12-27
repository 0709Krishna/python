year=int(input("Enter the year:"))
count=20
Leap_Count=0
print("Leap years:")
while(Leap_Count!=count):
    if((year%4==0 and year%100!=0) or (year%400==0)):
        Leap_Count+=1
        print(year)
    year=year+1