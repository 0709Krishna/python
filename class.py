class student:
    def __init__(self):
        print("Object is created")
std1=student()
print(std1)
std2=student()
print(std2)
print("-----------------------------------------------")
# Example for direct initialization
class student:
    def __init__(self):
        print("Object is created")
        #Direct initiaslization
        self.name="kavya"
        self.age=20
std1=student()
print("student Name :",std1.name)
print("student Age :",std1.age)
print("----------------------------------------")
std2=student()
print("student Name :",std2.name)
print("student Age :",std2.age)
print("----------------------------------------")
#with parameters
class student:
    def __init__(self,name,age):
        print("Object is created")
        self.name=name
        self.age=age
std1=student("krishna",20)
print("student Name :",std1.name)
print("student Age :",std1.age)
print("----------------------------------------")
std2=student("Radha",19)
print("student Name :",std2.name)
print("student Age :",std2.age)
print("-----------------------------------------------")
# Q) create Employee & declare the states of class as EmployeeName,EmployeeID,Designation,salary,location,special allowances i)create 3 objects &acces the values by using print function.
class Employee:
    def __init__(self,EmployeeName,EmployeeID,Designation,Salary,Location,Specialallowances):
        self.EmployeeName=EmployeeName
        self.EmployeeID=EmployeeID
        self.Designation=Designation
        self.Salary=Salary
        self.Location=Location
        self.Specialallowances=Specialallowances
emp1=Employee("fani",35,"HR",120000,"hyd",3400)
print("Employee Name:",emp1.EmployeeName)
print("Employee ID:",emp1.EmployeeID)
print("Designation:",emp1.Designation)
print("Salary:",emp1.Salary)
print("Location:",emp1.Location)
print("Special Allowances:",emp1.Specialallowances)
print()
# accessing values by using function name
def Display_Details(self):
    print("Employee Name:",emp1.EmployeeName)
    print("Employee ID:",emp1.EmployeeID)
    print("Designation:",emp1.Designation)
    print("Salary:",emp1.Salary)
    print("Location:",emp1.Location)
    print("Special Allowances:",emp1.Specialallowances)
Display_Details(emp1)
    

          
