
a = 123

#find the multiplication of digits of the number a
# 2 * 3 * 4 = 24

#When we find remainder with 10, it will give us the last
# digit of the number
#WHen I divide the number by 10, it will remve the last digit
last_digit = a%10 # gives 3
print(last_digit)
# Following line will remove the last digit of a variable
a = a // 10 # removes 3
middle_digit = a % 10 # gives 2bc its the last digit now
a = a //10 # get rids of the last digit
first_digit = a % 10 # gives 1 bc its the last digit now
multiplication = last_digit * middle_digit * first_digit # multiple each stored value of a 
print("Multiplication result of all digit is",multiplication)





#Integer divison will give us only the Integer part of the divison
#For Example
#21 /5 is 4.20 but if i use integer divison operator
# 21// 5 is 4


# b = 34
# print(b//10) 

# c = 67
# print(c//10)

# d = 105
# print(d//10)

# e = 1273
# print(e//10)