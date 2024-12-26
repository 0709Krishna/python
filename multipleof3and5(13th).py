num=int(input("enter the number:"))
if(num%3==0 and num%5==0):
    print(num,"is multiple of 3 and 5")
else:
    print(num,"is not multiple of 3 and 5")

print("-------------------------------------------------")
#using ternary operator
result="multiple of 3 and 5" if(num%3==0 and num%5==0) else "not multiple of 3 and 5"
print(result)