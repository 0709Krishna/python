list=['C','python','','','java','']
Null_Count=0
#condition to check number of null elements present in the list
for i in list:
    if(i==''):
        Null_Count+=1
print("Number of Null values are:",Null_Count)