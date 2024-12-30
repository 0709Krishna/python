Dict={101:'python',201:'java',301:'c',401:'flutter'}
print(Dict)
print(type(Dict))
print("-------------------------------------------")
print(Dict[101])
print(Dict[201])
print(Dict[301])
print(Dict[401])
Dict[501]='golang' # adding another element to dictionary
print("-----------------------------------------------")
print(Dict)
print("----------------------------------------")
Dict[101]='cython' # reassigning element to dictionary
print(Dict)
print("-----------------------------------------------------")
del Dict[401]   # deleting element in dictionary
print(Dict)
print("-------------------------------------")
#del Dict-->  delete entire dictionary
New_Dict=Dict.copy()
print(New_Dict)
Dict.update({301:'Gupchup'}) # update
print(Dict)
Dict.popitem() #popitem
print(Dict)
# Nested dictionary
nested_dict={'dict1':{'name':'krishna'},'dict2':{'name1':'priya'}}
print(nested_dict)