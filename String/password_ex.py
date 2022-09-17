
# Ask user to enter a password 
# If the password doesn't have any uppercase or doesn't have any lower case 
# print False, otherwise True.
print("Enter a password with upper and lower case letter:")
password = input()

is_there_upper = password != password.lower() 

# "PASSWORD
# will be equal to its upper case version
# If the password is not equal to its upper case version
# it means there is lower case in the string.

is_there_lower = password != password.upper()

is_valid_pass = is_there_lower and is_there_upper
print("Your password is valid",is_valid_pass)