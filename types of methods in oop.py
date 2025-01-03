# Instance variable with Instance method
class mobile:
    def __init__(self):
        self.model='RealMe x'
    def show_model(self):
        print(self.model)
realme=mobile()
realme.show_model()
r=realme.model
print("outside class:",r)
print("--------------------------------------")
# Instance variable with parameters
class mobile:
    def __init__(self):
        print('object is created...!')
        self.price=15000
    def show_price(self,price):
        print(self.price)
samsung=mobile()
samsung.show_price(1000)
# Accessor/getter method in Instance method
class markerpen:
    def __init__(self,color,price,brand):
        print('object is created...!')
        self.color=color
        self.price=price
        self.brand=brand
        #Accessor methods
    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def show_brand(self):
        return self.brand
m1=markerpen('Black',20,'camelin')
Res1=m1.show_color()
print(Res1)
Res2=m1.show_price()
print(Res2)
Res3=m1.show_brand()
print(Res3)
print("----------------------------------------------")
m2=markerpen('violet',20,'carbonix')
Res4=m2.show_color()
print(Res4)
Res5=m2.show_price()
print(Res5)
Res6=m2.show_brand()
print(Res6)
# Mutator/setter method in Instance method
class markerpen:
    def __init__(self,color,price,brand):
        print('object is created...!')
        self.color=color
        self.price=price
        self.brand=brand
    # Mutator method
    def set_color(self):
        self.color='Red'
    def set_price(self):
        self.price=25
    def set_brand(self):
        self.brand='Doms'
    #Accessor Methods
    def show_color(self):
        return self.color
    def show_price(self):
        return self.price
    def show_brand(self):
        return self.brand
m1=markerpen('Black',20,'camelin')
Res1=m1.show_color()
print(Res1)
Res2=m1.show_price()
print(Res2)
Res3=m1.show_brand()
print(Res3)
print("----------------------------------------------")
m1.set_color()
m1.set_price()
m1.set_brand()
Res1=m1.show_color()
print(Res1)
Res2=m1.show_price()
print(Res2)
Res3=m1.show_brand()
print(Res3)
print("--------------------------------------------------")
# class method with out  parameter
class mobile:
    @classmethod   #....>Decorator
    def show_model(cls):  #class method
        print("realme")
realme=mobile()
mobile.show_model()       #calling class method
print("----------------------------------------------")
class mobile1:
    fp='yes'  #class variable
    @classmethod
    def show(cls): #class method
    #Accessing class variable
        print("Fingerprint scanner:",cls.fp)
realme=mobile1()
mobile1.show()
print("-----------------------------------------------------------")
# static method
class watch:
    @staticmethod
    def showtime():
        print("watch shows time...!")
    @classmethod
    def showbrand(self):
        print("watch brand is rolex...!")
    def __init__(self,colour):
        print("object is created...!")
        self.colour=colour
    def get_colour(self):
        print(self.colour)
w1=watch('silver')
watch.showtime()
watch.showbrand()
w1.get_colour()
w1.showtime()
print("------------------------------------------------------------")
# All methods in single example
class student:
    @staticmethod
    def collegeName():
        print("ABC college...!")
    @classmethod
    def writeExams(self):
        print("Enjoy exams...!")
    # Accessor method
    def Show_Name(self):
        return self.studentName
    #Mutator method
    def set_Name(self):
        self.studentName='scott'
    def __init__(self,studentName,ID,Email):
        print('object is created...!')
        self.studentName=studentName
        self.Id=ID
        self.Email=Email
student.collegeName()
student.writeExams()
std1=student("kavya",130,"kavya@gmail.com")
print(std1.Show_Name)
        
