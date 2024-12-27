StudentName=(input("StudentName:"))#printing total and avg
Subject1=int(input("Subject1 Score:"))
Subject2=int(input("Subject2 Score:"))
Subject3=int(input("Subject3 Score:"))
print("student report:")
print("--------------------------------------------------")
print("StudentName:",StudentName)
print("Subject1:",Subject1)
print("Subject2:",Subject2)
print("Subject3:",Subject3)
if(Subject1>=35 and Subject2>=35 and Subject3>=35):
    Total=Subject1+Subject2+Subject3
    print("Total:",Total)
    Average=(Total)/3
    print("Average:",Average)
    if(Average>=90):
         print("Congratulations you have qualified with 1st class")
    elif(Average>=75):
        print("Congratulations you have qualified with 2nd class ")   
    else: 
        print("Congratulations you qualified with 3rd class")
else:
     print("Better luck next time")
    

