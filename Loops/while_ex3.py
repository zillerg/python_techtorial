

# You have $40 in your phone account.
# After each call you'll be charged $5 
# print -> how much calls you can make
# and how much money is left after each call


phone_acc = 40
call = 3
number_of_calls = 1
money_left = 0

while phone_acc >= call:
    print(f"{number_of_calls} call is made")
    number_of_calls += 1
    phone_acc -= call
    print(f"After the call I have ${phone_acc} left")   