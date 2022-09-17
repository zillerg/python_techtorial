
# Ask user to enter two numbers 
# one smaller than the other
# print sum of all the numbers that are divisible by 2 and 7 between
## the given two numbers
# For ex:
# 2 50
# output: 14 + 28 + 42 = 84

print("enter a number")
num = int(input())

print("enter a number bigger than first one")
num2 = int(input())
sum =0
text = ""
for n in range(num,num2):
    if n % 7 == 0 and n % 2 == 0:
        text = text + str(n) +  " + "
        sum+=n

print(text.removesuffix(" + "),"=" , sum)



# print("Enter a number")
# num1 = int(input())

# print("enter a bigger number")
# num2 = int(input())
# sum = 0
# text = ""
# for n in range(num1, num2):
#     if n % 7 == 0 and n % 2 == 0:
#         text = text + str(n) + " + "
#         sum += n

# print(text.removesuffix("+ "),"=", sum)








# Inventory_item1 = "milk"
# Inventory_item2 = "butter"
# Inventory_item3 = "coffee"
# Inventory_item4 = "milk"

#inventory_items = ["milk", "butter","coffee","sugar","sugar"]

#print(type(inventory_items)) --> class.'list'











