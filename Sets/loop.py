
# is set object is iterable?
# seet object is iterable
s1 = {"new","value2","value3","value4"}

# Sets don't have index numbers.
# Can't use while loops with Sets

for element in s1:
    print(element)
   
# String is an iterable object 
# string is ordered, so it has index numbers .
str = "Python"
s2 = set(str)

print(s2)  # {'n', 't', 'h', 'o', 'y', 'P'}
print(str) # Python

# If you want to get first element from the str ? 
print(str[0])  # P

# If you want to get first element from the list? 
#print(s2[0]) #it will throw an error

index = 0
while index < len(str):
    print(str[index])
    index+=1

for x in str:
    print(x)

for element in s2:
    print(element)

# This line will throw an error because we cannot use 
# index numbers with set.
# index =0
# while index < len(s2):
#     print(s2[index])

# len()

print(len(s2)) #It will print the size of s2 which is a set


















