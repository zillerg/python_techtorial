
# In the factory we need to create a program that can 
# find if we can do the shipment and if we can do the shipment
# it will tell use how many small package we should ship.
# First we need to get total kilogram of the shipment,
# to reach this total kilogram of shipment we can use small and big packages. 
# Every big package is 5 kilogram and every small packages is 1 kilogram.
# We have limited amount of small and big packages. 
# Ask user how many big and how many small package  they have.
# Ask user what is the total goal kilogram of the shipment.
# Print whether they can ship, if they can ship print how many small packages they need. 
# Assume big packages is used before small packages. 

# count of small package = 4 -> 4 kilogram
# count of big package = 1 -> 5 kilogram 
# goal is to ship 9 kilogram 
# i can ship and i need to use 4 small package

# 5 small package-> i need to use 3 smal package
# 4 big package  -> how many big package i need to use -> 2
# I need to ship 13 kilogram 
# i can ship and i need to use 3 small package

# 3 small package-> i need to use 4 small package to complete but since i don't 
# have 4 small package i cannot ship
# 3 big package -> i can use max 2 big package
# i need ship 14 kilogram
# I cannot ship

print("Enter the kilogram we need to ship")
goal_ship = int(input()) # 12

print("Enter amount of small packages you have")
count_of_small = int(input())

print("Enter amount of big packages you have")
count_of_big = int(input())

# I have to start from big packages to reach goal kilogram
# How can I find how many big package i need to reach to goal?

needed_big_packages = goal_ship // 5


# If I don't have enough big packages can I do the shipment-No

# 9 small package
# 1 big package 
# I need to ship 14 kilogram
if needed_big_packages<=count_of_big:
    #How many small package i need
    needed_small_packages = goal_ship%5
    if needed_small_packages <= count_of_small:
        print(f"I can do the shipment and i need {needed_small_packages} amount of small package")
    else:
        print("I cannot do the shipment")
else:
    # How many kilogram can I reach with the big boxes i have  and then the rest of the amount i will 
    # try to complete with using small packages
    kilogram_i_have = count_of_big * 5;
    left_goal = goal_ship - kilogram_i_have
    # Left goal divided by 1 will give amount of small package i need 
    if left_goal<=count_of_small:
        print(f"I can do the shipment and I need {left_goal} amount of small boxes")
    else:
        print("i cannot do the shipment.")