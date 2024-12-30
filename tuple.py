tuple=(10)
print(type(tuple))
#with multiple elements
tuple1=(10,-60,21.3)
print(type(tuple1))
print('------------------------------')
#Typle packing
Tuple='python','c','c++'
print(Tuple)
print(type(Tuple))
print("----------------------------------")
#Tuple unpacking
percentages=(99,95,90,89,93,96)
a,b,c,d,e,f=percentages
print(c)
print("---------------------------------------")
#Accesing tuple
Tuple1=('python','c','c++','java','dart','flutter')
print(Tuple1[0])
print(Tuple1[-4])
print(Tuple1[-6])
print(Tuple1[3])
print("------------------------------------")
#Accessing tuple elements using for loop
Tuple2=('python','c','c++','java','dart','flutter')
for i in Tuple2:
    print(i)
print("-------------------------------------")
#Accessing tuple elements using while loop
i=0
while(i<len(Tuple2)):
    print(Tuple2[i])
    i+=1
print("---------------------------------------")
# Tuple Slicing
Tuple3=(11,22,33,44,1,2,3,4,5,5,10,15,20,25,30)
print(Tuple3[3:])
print(Tuple3[0:15:1])
print(Tuple3[:6])
print(Tuple3[::-1])
print("---------------------------------------------------")
#Tuple concatenation
a=(10,20,30)
b=(4,5,6)
Tuple4=a+b
print(Tuple4)
print("-------------------")
#Tuple deleting
Tuple5=(10,20,-20,56.1)
del Tuple5
print("-------------------------------")
#Repetition of tuple
b=(1,2,3)
result=b*3
print(result)
print("----------------------------")
# Nested tuple
Tuple=((1,2,3),(4,5,6),(7,8,9))
print(Tuple)
print(Tuple[0])
print(Tuple[0][1])
print(Tuple[1][1])