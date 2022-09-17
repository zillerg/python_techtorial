
# Ask user to give you two integer numbers.
# Fiid the sum of these two integer numbers.
# If sum of these two integer is smaller than 10
# print sum of these two number is 10
# If sum of these number is between 10  - 19 inclusive
# print sum of these two numbers is 20
# For all other conditions print the actual sum of these two numbers



print("Enter first number")
num1 = int(input())
print("Enter second number")
num2 = int(input())

sum = num1 + num2

if sum < 10 :
    print("sum of these two number is 10")
elif sum >= 10 and sum <= 19:
    print("sum of these two numbers is 20")
else:
    print(sum)