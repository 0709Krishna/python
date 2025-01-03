# Duck Typing
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak tabdak")
def myfunction(obj):
    obj.walk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
print("--------------------------------------------------------------------")
# Another Examlple
class Father:
    def work(self):
        print("Hard working Father!")
class Son:
    def work(self):
        print("Enjoying Son!")
def Result(self):
    self.work()
F1=Father()
Result(F1)
S1=Son()
Result(S1)
        