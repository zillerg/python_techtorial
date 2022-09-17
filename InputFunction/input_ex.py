# User wants to deposit his money to his account
# he already has $200 in his account
# He has three different paycheks (400, 600 and $350)
# He can only deposit one paycheck at a time
# After he deposits all the money in the account
# He bought a phone for $599 and headphone for $299
# Create a python program to calculate his final money in the account
# Use input function to get all the values

bank_acc = 200
print("Please enter the first paycheck amount you want to deposit")

first_deposit = int(input())

bank_acc += first_deposit

print("Please enter the second paycheck amount you want to deposit")

second_deposit = int(input())

bank_acc += second_deposit

print("Please enter the third paycheck amount you want to deposit")

third_deposit = int(input())

bank_acc += third_deposit

print("Please enter the dollar amount of phone you want to buy")
phone = int(input())

bank_acc -= phone

print("Please enter the dollar amount of headphone you want to buy")

head_phone = int(input())

bank_acc -= head_phone

print("His final money in the bank account is", bank_acc)

#------------------------------------------------
# --------------My code----------------
# bank_account = 200
# print("First how much money you want to deposit?")
# first_check = input()
# print("Second how much money you want to deposit?")
# second_check = input()
# print("Third how much money you want to deposit?")
# third_check = input()
# phone_price = 599
# headphone_price = 299

# bank_account = bank_account + int(first_check)
# bank_account = bank_account + int(second_check)
# bank_account = bank_account + int(third_check)

# bank_account = bank_account - phone_price - headphone_price
# print("This is the account balance after your purchase: ", bank_account)