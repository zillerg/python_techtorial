
s = "Techtorial"

print(s[4:7])
print(s[4]+s[6])

# Ask user to enter a string which length is odd and longer than 3
# and print the middle three letters from the string

print("Enter a string which length is odd and longer than 3 letters")
text = input()
#First i have to find middle index
middle_index = len(text) // 2  #int(len(text)/2)

print(text[middle_index - 1: middle_index + 2])


# Ask user to enter a string which length is even and longer than 4
# and print the middle 4 letters from the string

#Techtorial -> htor
# keyboard -> yboa
print("Enter a string which length is even and longer than 4 letters")
text = input()
middle_index = int(len(text) / 2)

print(text[middle_index - 2: middle_index + 2])