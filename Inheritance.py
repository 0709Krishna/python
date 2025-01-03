# Single and Multilevel inheritance
class vehicle:
    def __init__(self):
        print("Hey I 'm the vehicle class constructor..!")
class Bike(vehicle):
    def __init__(self):
        super().__init__()
        print("Hey I'm the Bike class constructor..!")
class SuperBike(Bike):
    def __init__(self):
        super().__init__()
        print("Hey I'm the Super Bike class constructor...!")
s1=SuperBike()
# Hierarchical inheritance
class engineer:
    def __init__(self):
        print("I 'm the engineer class constructor")
e1=engineer()
print("-----------------------------------------------------")
class softwareengineer(engineer):
    def __init__(self):
        super().__init__()
        print("I 'm the softwareengineer class constructor")
sel=softwareengineer()
print("--------------------------------------------------")
class civilengineer(engineer):
    def __init__(self):
        super().__init__()
        print("I 'm the civilengineer class constructor")
c1=civilengineer()
print("------------------------------------------------")
class mechanicalengineer():
    def __init__(self):
        super().__init__()
        print("I 'm the mechanical engineer class constructor")
m1=mechanicalengineer()
# hybrid and multiple inheritance
class A:
    def __init__(self):
        print("class A")
class B(A):
    def __init__(self):
        super().__init__()
        print("class B")
class C(A):
    def __init__(self):
        super().__init__()
        print("class C")
class D(B,C):
    def __init__(self):
        super().__init__()
        print("class D")
c1=C()
d1=D()
