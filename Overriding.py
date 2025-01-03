# Overriding
class Engineer:
    def work(self):
        print("Engineer")
class SoftwareEngineer(Engineer):
    def work(self):
        print("Software Engineer")
class ElectricalEngineer(Engineer):
    def work(self):
        print("Electrical Engineer")
E1=Engineer()
E1.work()
Se1=SoftwareEngineer()
Se1.work()
Ee1=ElectricalEngineer()
Ee1.work()