
# len() function allows us to learn how many charachters used to create string
# length function counts spaces as well.

str = "Techtorial"
str1 ="Techtorial "

print(len(str))
print(len(str1))

# length function will return an integer value so we can assign integer variables using
# length function
length_of_the_str = len(str)
print(length_of_the_str)
print(type(length_of_the_str))

# Create a program ti pring True if length of str is even number
#Even number can be divided by 2
is_length_even = length_of_the_str % 2 == 0
print(is_length_even)
