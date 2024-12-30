set={30,78.9,34+76j,"hello krishna"}
print(set)
print(type(set))
# print(set[0]) is not possible
print("----------------------------------------")
# Add in set(used for onlly 1 element to add)
set.add('Purple')
print(set)
set.add('Orange')
print(set)
#Adding multiple elements
set1={'lavender','indigo','rosegold','peach'}
set.update(set1) 
print(set)
print("------------------------------------")
# Duplicates are avoided
b={10,20,'students',40,10,10}
print(b)
print("-----------------------------------")
# Creating empty set---> x=set()
# set methods
a={'rahul','raj','sonam','rani'}
b={'sumit','rahul','rani','python','java'}
print("A:",a)
print("B:",b)
print()
#intersection() method--> returns item which exists in both sets
ism=a.intersection(b)
print("intersection:",ism)
print()
# Union method--> returns all item from original set and all items from specified set
um=a.union(b)
print("Union:",um)
print()
# Difference() method--> returns items that exists only if first set,and not in both sets
dm=a.difference(b)
print("Difference:",dm)
print()
# issubset() method--> returns true if all items in set exists in specified set
issub=a.issubset(b)
print("issubset:",issub)
print()
# issuperset() method--> returns true if all items in specified set exist in original set
issup=a.issuperset(b)
print("issuperset:",issup)
print()


