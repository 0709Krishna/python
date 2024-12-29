#number/character
str='5'
print(str.isalnum()) # isalnum()-->returns true if string is alphabet or numeric
print(str.isalpha())
print(str.isdigit())
print(str.isnumeric())
print(str.isdecimal())
print("--------------------------------------------------------------------------------")
# write pp to check whether user entered character is a alpabet or digit or decimal
str1='krishna'
for i in str1:
 if str1==str1.isalpha():
        print(str1.isalpha())
 elif str1==str1.isdigit():
     print(str1.isdigit())
 else:
     print(str1.isdecimal())
print('------------------------------------------------------------------')
# wrie a pp to print no of vowels & consonents present in user entered string
str2=input("enter the string:")
vowel_count=0
consonent_count=0
for i in str2:
    if(i in ('A','E','I','O','U','a','e','i','o','u')):
        vowel_count+=1
    else:
        consonent_count+=1
print("vowel count is:",vowel_count)
print("consonent count is:",consonent_count)
print('-------------------------------------------------------------')
#space/strip
str3="                python              "
print(str3)
print(str3.lstrip()+'i')
print(str3.rstrip()+'i')
print("---------------------------------------------------------------")
#with special characters vowels & consonents
str4=input("Enter the string:")
str4=str4.lower()
str2=str4.replace(' ','')
vowel_count=0
consonent_count=0
for i in str4:
    if(i in ('a','e','i','o','u')):
        vowel_count+=1
    elif(i.isalpha()):
        consonent_count+=1
print("vowels count:",vowel_count)
print("consonents count:",consonent_count)
print("-------------------------------------------------------------------")
#wrie pp to print alphabets,special characters,digits present in user entered string
str5=input("enter the string:")
str5=str5.lower()
str5=str5.replace(' ','')
alpha_count=0
special_count=0
digits_count=0
for i in str5:
    if(i.isalpha()):
        alpha_count+=1
    elif(i.isdigit()):
        digits_count+=1
    else:
        special_count+=1
print("vowels count is:",alpha_count)
print("digits count is:",digits_count)
print("special count is:",special_count)

        

        
