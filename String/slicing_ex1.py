
# Ask user to enter a string and print a rotated let 2 version
# where the 2 chars moved to the end.

# 'Hello' -> 'lloHe'
# 'java'  ->  'vaja'
print("Enter the string here:")
string = input()

first_two_letters = string[:2]
rest_of_the_string = string[2:]

string = rest_of_the_string + first_two_letters

print("The string is ",string)
