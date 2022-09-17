
print("Enter number")
num1 = int(input())
print("Enter number")
num2 = int(input())
print("Enter number")
num3 = int(input())

list = [num1,num2,num3]

sum_of_numbers = []
for i in list:
    remainder = i % 10
    if remainder >= 5:
        sum.append(i + 10 - remainder)
    elif remainder <= 5:
        sum.append(i - remainder) 
whole_sum= sum_of_numbers[0] + sum_of_numbers[1] + sum_of_numbers[2]   

print(whole_sum)           
    

