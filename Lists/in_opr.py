

#Using in operator we can check specified value is in the list
# or not.
# We can also user in operator for strings as well.
# We can use operator in any iterable object

list = [1,2,3,4,5]


if 2 in list:
    print("2 is in the list")

if 11 in list:
    print("11 is in the list")    
    # 11 is not in the list.
# not in operator will check if the specified value is not in the stiring
# iterable objects.

if 6 not in list:
    print( 6, "is not in the list")

# ask user to enter a random digit
# check if the digit is present in our list or not.
# if user enters present element print you won
# if not print maybe next time

print("enter a random digit")
digit = int(input())

if digit in list:
    print("You have won the prize")
elif digit not in list:
    print("Maybe next time.")


# in operator can be used for every iterable object.












