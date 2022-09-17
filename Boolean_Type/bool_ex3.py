
#Veera wants to lose 10 pounds in one month.
# There are multiple conditions to lose 10 pounds in a month
# Veera needs to walk 10000 steps daily OR needs to run at least 4 miles a day
#and Addition to those, Veera needs to eat less then 1500 calories a day.
# Create a program to calculate if Veera can lose weight or not.

walking_steps = 5000
running_distance = 4
daily_calories = 1500

can_lose_weight = (walking_steps >= 10000 or running_distance >= 4) and daily_calories <= 1500

print("Veera can lose weight", can_lose_weight)


