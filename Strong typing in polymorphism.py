# Strong Typing
class Duck:
    def walk(self):
        print("thapak thapak thapak thapak thapak")
class Horse:
    def walk(self):
        print("tabdak tabdak tabdak tabdak tabdak")
class cat:
    def talk(self):
        print("Meoww Meow")
def myfunction(obj):
    if hasattr(obj,'walk'):
        obj.walk()
    if hasattr(obj,'talk'):
        obj.talk()
d=Duck()
myfunction(d)
h=Horse()
myfunction(h)
c=cat()
myfunction(c)

        