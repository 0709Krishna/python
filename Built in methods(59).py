#Example for list methods
cartoons=['tom & jerry','krishna aur balaram','chotabheem','dora','shinchan','benten','little krishna']
print("cartoons")
print("afer appending an element:")
cartoons.append('oggy & cockroaches')
print(cartoons)
print("after inserting the element:")
cartoons.insert(2,'roll no 21')
print(cartoons)
print("after pooping the element:")
cartoons.pop()
print(cartoons)
cartoons.remove('chotabheem')
print(cartoons)
print(cartoons.index('tom & jerry'))
print("after reversing the list:")
cartoons.reverse()
print(cartoons)
#extend
a=[2,4,6,8,10]
b=[1,3,5,7,9]
print(a)
print(b)
a.extend(b)
print(a)
b.extend(a)
print(b)
#count---->list.count(element)
count=b.count(10)
print(count)
count=a.count(6)
print(count)
print('---------------------------------------------------')
#sort()
n=[90,78,45,67,23,12,34,60]
print(n)
print("Sorted List:",n)
l1=['K','A','O','Y','C','h','f','m']
print(l1)
l1.sort()
print("sorted list:",l1)
print("------------------------------------------")
#repeat same value
n=[3,6,9]
print(n*10)