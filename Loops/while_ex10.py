
# Ask user to enter a string
# If the given string contains any duplicated letter
# print string has duplicated letter
# otherwise print string consists of unique letters

print("Enter a string")
str = input()

# We should check for each letter, iif theres a duplication
is_unique = True
index = 0
while index < len(str):
    if str.count(str[index]) > 1:
        # it means theres a duplicated letted
        is_unique = False
        break
    index += 1    

if is_unique:
    print("String consists of unique letters")
else:
    print("String has duplicated letters")


# range function in python
# Range is one of the built in function in python

# syntax -> range(5)
# this will give you numbers between 0 and 4 inclusive

# You can also choose where do you want range function to start
#range(1,6)
#this will give you numbers between 1 and 5 inclusive
# You can also give incrementing step for range function
# range (3,12,2)
# This will give you 3 5 7 9 11

# range(3,12,2)
# This will give 3 6 9

# Range function will only work with Integer numbers.

# print(type(range(5)))
# It will be range class. range function returns a range object.


# Iterable objects in python are strings, tuples, lists and arrays
# Which means they can be used with for loop and we can iterate in 
# individual elements from them.

# For Loop
# It works with iterable objects and gets in individual elements 
#from iterable objects and allow us to modify the individual objects.

#str = "Techtorial"

# Print each letter from str

# index = 0
# while index < len(str)
#   print(str[index])
#   index += 1

#Print each letter from str
# for i in str:
#    print(l)
#    print(type(l)) # String

#for x in range(5):
#    print(x)
# 0 1 2 3 4

#print all the even numbers from 2 to 20
#for x in range(2,21,2):
#   print(x)
# 2 4 6 8 10 12 14 16 18 20  
# 
# Print all the even numbers from 2 to 20 inclusive
# without using step in the range function
# for x in range(2,21):
#    if x % 2 == 0:
#       print(x)
