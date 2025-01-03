Num=99
def Disp():
    global Num # global in local
    print(Num)
    Num=999
    print(Num)
Disp()
    