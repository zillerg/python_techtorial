
# Given a string, return a version where all the "x" have been removed.
# Except an "x" at the very start or end should not be removed

# "xxHxix" -> "xHix"
# "abxxxcd" -> "abcd"
# "xabxxxcdx" -> "xabcdx"

print("Enter a text with x'es")
str = input()
# We do not need to change first and last chars of the string

first_ch = str[0]
last_ch = str[-1]
middle_str = str[1:-1]
middle_str = middle_str.replace("x","")

print(first_ch+ middle_str + last_ch)