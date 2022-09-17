
# Ask user to enter an integer number
# and print multiplication table for given number


# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# ........
# 3 * 10 = 30



print("Please enter integer number")
num = int(input())

max_table = 10
mulitplication = 1
while mulitplication <= max_table:
    print(f"{num} * {mulitplication} = {num * mulitplication}")
    mulitplication += 1
    