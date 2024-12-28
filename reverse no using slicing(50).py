Num="123456"
#conversion str to list
List_Num=list(Num)
print(Num)
print(List_Num)
Res=''
for i in List_Num:
    Res=i+Res
print(Res)