# Ask user to give string 
# Ask user to give order number of the letter and print that letter from the string


print("Enter a text:")
text = input()

print("Enter the order number of the letter you want to see")

order_number = int(input())

# We have to consider that user doesn't know about index numbers and the number user provided will be
# 1 bigger than the index number
# "Python"
#  012345 -> index numbers
#  123456 -> order number which user will think it is true

index_number = order_number - 1

print(text[index_number])