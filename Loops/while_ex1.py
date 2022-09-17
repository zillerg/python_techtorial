
# Ask user to give you a string
# from that stirng print index numbers of all the e's
#

print("Enter a string")
str = input()

# We can access string elements using thier indexes.
index = 0

#Index number is always smaller than length of the string

length_of_str = len(str)

while index < length_of_str:
    # I want to access element with an index number
    if str[index] == "e":
        print(f"Index number of e is {index}")
    index += 1