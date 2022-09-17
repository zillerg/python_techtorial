

# isalpha() method
# It only returns True when all chars of the string is letters.

s = "This is text"
print(s.isalpha())
# False and the reason for that is spaces are not considered as letters.

#s = s.replace(" ","")
print(s.replace(" ","").isalpha())
#True bc using replace method we remove all the spaces from the string.

print(s.replace(" ","-").isalpha())
# It eill print False bc -> it is not letters

print(type(s.isalpha())) # class<bool>


#isnumeric() only return True when all chars are numeric
s1 = "777-777-7777"
print(s1.isnumeric)
# False bc -> is not numeric type.

print(s1.replace("-","").isnumeric())
# True
s1 = "777b4eh3"
print(s1.isnumeric())
# It will return False


#isalnum checks if the entire string consists of letters and numbers
print(s1.isalnum())
# it will print True
s1 = "777-777-7777"
print(s1.isalnum())
# False bc it has ---

# it doesn't have to containt both letter and number at the same time.
# even if it has only one of the type it will return True.
s2 = "string"
s3 ="777777"
s4 = "478eiuhjr847iu"
s5 ="ksjadl45-"
print(s2.isalnum())   # True
print(s2.isnumeric()) # False
print(s2.isalpha())   # True
################################
print(s3.isalnum())   # True
print(s3.isnumeric()) #True
print(s3.isalpha())   #False
################################
print(s4.isalnum())   # True
print(s4.isnumeric()) # False
print(s4.isalpha())   # False
################################
print(s5.isalnum())   # False
print(s5.isnumeric()) # False
print(s5.isalpha())   # False