
# The doctors say you babies can go out in summer if the weather is
# between 60 and 80 inclusive. If not they say you shouldn;t take the baby out.
# In the winter they say you can go out if the weather is hotter than -20
# Ask user what season they are in also ask user how the weather
# is and print if they can go out with baby or not.

print("What season are you in?")
season = input()

print("How hot is the weather?")
w = int(input())

# if user enters SuMMEr
if season.lower() =="summer":
    #If this line is getting executed, it means season is summer.
    if w<=80 and w>=60:
        print("You can take the baby out.")
    else: 
         print("You shouldn't take the baby out.")
elif season.lower() =="winter":
    if w > -20:
        print("The babies can go out.")
    else:            
         print("You shouldn't take the baby out.")


# print("What season are you in?")
# season = input()

# print("How hot is the weather? ")
# weather = int(input())

# # If user enters summer
# if season.lower == "summer":
#     # If this line getting executed it means season is summer.
#     if weather <= 80 and weather >= 60:
#         print("You can take the baby out.")
#     else:
#         print("You shouldn't take the baby out")
# elif season.lower == "winter":
#     if weather > -20:
#         print("The babies can go out.")
#     else:
#         print("You shouldn't take the baby out")