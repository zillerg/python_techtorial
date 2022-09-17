
# Ask user to give two different string values
# If the first string contains the second string
# return True, if not return False
print("Enter first string:")
s = input()
print("Enter second string:")
s2 = input()

count_of_str = s.count(s2)
is_contains = bool(count_of_str)#count_of_str > 0
print(is_contains)

# If the first string doesn't contain the second string
# count of the second string in the first one should be 0

