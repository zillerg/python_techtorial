
# Ask user to enter an integer number and print out 
# all the divisor of given number

# Possible dividers of given number
# starts from 1 -> ends at the given number itself


print("Enter any number")
num = int(input())
possible_divisers = 1

s = ""

while possible_divisers <= num:
    # Since we have possible deviser, but we are not sure if we can divide num or not
    # how can i understand if possible deviser is an actual divisor of the number?
    # If the number % possible disivor is 0  it means possible_deviser
    # is an actual diviser number
    if num % possible_divisers == 0:
        s += str(possible_divisers)+", "
        #print(f"{possible_divisers} is a divisor of the number")  
    possible_divisers += 1
print(s.removesuffix(", "),"are the divisors of the number")