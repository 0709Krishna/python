#creation of list
prog=['c','c++','java','python','html','css','java script','angular','react js']
print(prog)
print(type(prog))
print("------------------------------------------------")
# Iterating through list elements without index
for i in prog:
    print(i)
print("------------------------------------------------")
#Iterating through list elements with index
for i in range(len(prog)):
    print(prog[i])
print("------------------------------------------------")
# Iterating using while loop
index=0
while index<len(prog):
    print(prog[index])
    index+=1
    