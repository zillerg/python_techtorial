
num1 = 5
num2 = 7

if num1 < num2:
    print(f"{num1} is less than {num2}")

# What is the result of num2 < num1 -> False
if num2 < num1:
    print(f"{num1} is less than {num2}") # This line will not get printed

# if statement will execute the next line only when the given condition is
# True
is_num2_bigger = num2 > num1

if is_num2_bigger:
    print("num2 is bigger than num1")

#print("I recently bought {} product it was brand new it costed me {}$ and it was deliverd on {}".format(num1, num2))

# Ask user to enter a string
# If user enters a string with all lower cases print you entered correct cases
print("Enter a stirng")
str = input()
is_lower = str.islower()

if is_lower:
    print("You entered correct answer")
    print("because you entered all lower")
print("you entered a stirng")

# Line number 1 and 2 are inside the if statement so they will depend on condition, 
# but line number 3 is outside of if statement(no indentation) therefore
# line number 3 doesn't depend on any condition