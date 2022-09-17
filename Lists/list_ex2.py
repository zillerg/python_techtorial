

nums = [1,2,10,11,13,17,21,26]

# From the given list find sum of all the even numbers
# lets find sum of all the odds separetly
sum_odd = 0
sum = 0
for i in nums:
    if i % 2 == 0:
        sum += i
    else:
        sum_odd += i    
print(f"Sum of even numbers {sum} and sum of odd numbers {sum_odd}")





















