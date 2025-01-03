# Overloading is not support in python
class demo:
    def display():
        print("I m a zero argument method")
    def display(a,b):
        print("I m a one argument method")
demo.display(1,2)