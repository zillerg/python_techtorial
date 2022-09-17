
s = "Python"

print(s.upper()) # -> PYTHON

print(s)    # -> Python
# Since the string is immutable, it will not change its value unless it is reassaigned.

s = "PYthon"
print(s.lower())

# Method chaining -> as long as the method you use in the string return another string
# You can use other string methods
print(s.lower().upper()) # s will be printed in all upper case since it is the last method

print(s.lower().upper()[::-1]) # Chained with advanced slicing and reversed

print("Result of swap case method", s.swapcase())

print("Result of capitalize method", s.capitalize)
