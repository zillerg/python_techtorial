
# Ask user with given string, duplicate each letter in given string
# input -> abc
# output: aabbcc
# input def
# output ddeeff


print("Enter a string")
str = input()

duplicated = ""

for i in str:
    duplicated += i
    duplicated += i

print(duplicated)





















