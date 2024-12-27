# write python program to read the employee name,designation,salary,special allowances,bonus as input from user
#Gross monthly salary
Emp_Name=input("Employee Name:")
Designation=input("Designation:")
Special_Allowances=int(input("Special Allowances:"))
Salary=int(input("Salary:"))
Bonus=int(input("Bonus:"))
print("Emp_Name:",Emp_Name)
print("Designation:",Designation)
print("Special Allowances:",Special_Allowances)
print("salary:",Salary)
print("Bonus:",Bonus)
Gross_monthly_salary=(Salary+Special_Allowances)
print("gross monthly salary is:",Gross_monthly_salary)
print("------------------------------------------------------------------------")
#Gross annual salary
Emp_Name=input("Employee Name:")
Designation=input("Designation:")
Special_Allowances=int(input("Special Allowances:"))
Salary=int(input("Salary:"))
Bonus=int(input("Bonus:"))
print("Emp_Name:",Emp_Name)
print("Designation:",Designation)
print("Special Allowances:",Special_Allowances)
print("salary:",Salary)
print("Bonus:",Bonus)
Gross_annual_salary=(Gross_monthly_salary*12+Bonus)
print("gross annual salary is :",Gross_annual_salary)
print("------------------------------------------------------------------------")
#calculating taxable income
Taxable_Income=0
if(Salary>500000):
    Taxable_Income=Gross_annual_salary*0.5
    print("Taxable_Income:",Taxable_Income)
elif(Salary>400000):
    Taxable_Income=Gross_annual_salary*0.10
    print("Taxable_Income:",Taxable_Income)
else:
    Taxable_Income=Gross_annual_salary*0.2
    print("Taxable_Income:",Taxable_Income)
    
    
