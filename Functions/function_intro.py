

# When we want to reuse the piece of code or algorithm
#we create function and reuse them

# syntax of creating a function is -> def


def print_name():
    print("Techtorial.")
# Method only work when they get called.
print_name()

#Let's create a method for greeting.
# It will take user's name as argument and will print, hello and username

def greeting(name):
    print(f"Hello {name}")

#Not a good practice to put input() inside method.
print("Enter your name:")
user_name = input()

greeting(user_name)



print(type(greeting(user_name)))


def get_greeting(name):
    return f"Hello {name}"


#Methods includes what is indented but it is 
#recommended to skip two lines of code after last line method.
print(type(get_greeting("John")))
greeting1 = get_greeting("John")
print("Type of greeting is",type(greeting1))
print(greeting1)

print(get_greeting("Yusuf"))
print(get_greeting("Zalkar"))
print(get_greeting("Steve"))


# Create a method to fund sum of given two integers.
#Given always means method will take  it as parameter.
# Add if statement in this method so it will print error ocurred if type of num1 or type of num2 is not float or integer
def sum(num1, num2):
    addition = num1 + num2
    s = str(type(addition))
    if "int" in s or "float" in s:
        return addition
    else:
        return "An error occurred"    
    # if type(num1 + num2) != float or int:
    #     return "Error ocurred"
    # Methidds will always stop when code reaches the return statement

print(f"The sum of these numbers is {sum(2,3)}")




def sum2(*nums):
    sum = 0
    for element in nums:
        sum += element
    return sum    

print(sum2(1,5,6,8,9))
