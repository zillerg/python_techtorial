
# Ask user to enter two numbers
# First is greater than second one
# Find out sum of all numbers between given two numbers

# first number is 7
# second number is 3
# 3 4 5 6 7 -> 15
#  first number is 9
# second number is 6
# 6    7 8     9 -> 15
# first is 11
# second is 7
# 7   8 9 10   11 -> 27

print("Enter first number: ")
num1 = int(input())

print("Enter number smaller than first: ")
num2 = int(input())

#Before we get to the sum let's print all the numbers between two given numbers
copyOfNum2 = num2
num2 = num2 + 1
sum = 0
while num2 < num1:
    #print("in the loop",num2)
    sum += num2
    num2 = num2 + 1    
print(f"Sum of the numbers between {num1} and {copyOfNum2} is {sum}")
    
    





















