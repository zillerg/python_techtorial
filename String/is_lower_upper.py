
s = "Python"
print(s.islower())
# False bc, it return True when the string has only lower case letters
print(s.lower().islower())
# True bc the lower method makes all letter in lower case
s.upper() # Using methods in string will not effect the original
# value of the string.
print(s.isupper())
# False


# Ask user to enter their name in uppercase
# if they didn't enter in upper case print falsee

print("Enter your first name in upper cases")
first_name = input()

print(first_name.isupper())