
str = "hello"
str1 = "hello"
str2 = "heLlo"
#Equal sign is case sensative, so if cases of the two string is different
#it will return false
print(str == str1)
print(str1 == str2)

# We can reassign and change the string values as we were able to do with other
# data types

str2 = "hello"
print(str2) #hello

#Since we reassign and change the value of the str2
# comparison between str2 and str1 will give result as True
print(str2 == str)


#Concatenating the String
# Concatenating is adding more string to the existing string value
str2 = str2 + " world"
print(str2) # hello world

# We can use concatentaion even when we are creating the sting variable first time.

str3 = "hello" + " world"
print(str3) # hello world

str4 = str + str1
print(str4)