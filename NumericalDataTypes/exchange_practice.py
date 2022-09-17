

# Create a python program to give
# most efficient exchange possible using only 
# coins
# quarter 25 cents
# nickel 5 cents
# dime 10 cents
# penny 1 cent
# 2.34 cents of exchange
# 9 quarters 
# 0 dimes
# 1 nickel
# 4 pennies
# $1.89 
# 7 quarters 1 dime and 0 nickels 4 pennies
dollar = 2.96
#print(type(dollar))
dollar_amount = dollar * 100
#print(type(dollar_amount))
quarter = 25
dime= 10
nickel = 5
penny = 1
    
count_of_q = dollar_amount // quarter # We get the maximum amount of quarters here
    # // Integer divison gives us only Integer value of 11

print("We need to give back",count_of_q, "quarters") # Hence we get 11 here
            
remaining_exchange_after_q = dollar_amount % quarter
# We have to get remainder to count how many nickel, dimes and pennies we have to give
#remainder is 21

count_of_dime = remaining_exchange_after_q //dime 
# We count 21 // 10 and get 2
print(count_of_dime,"dimes")
remaining_exchange_after_d = remaining_exchange_after_q % dime
# remanider for 21 

count_of_nickel = remaining_exchange_after_d // nickel
print(count_of_nickel,"nickels")
remaining_exchange_after_n = remaining_exchange_after_d % nickel

count_of_pennies = remaining_exchange_after_n // penny
print(count_of_pennies,"pennies")
remaining_pennies = remaining_exchange_after_n % penny