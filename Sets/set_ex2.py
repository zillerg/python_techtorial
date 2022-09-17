

s = {2,2,3,4,5,7}
s2 = {4,10,2,5,44}
print(min(s))

# find out min number from the s and 
# mulitple with max number of s2
min = 0
max1 = 0
# In the first iteration of the loop I should
# change the value of the min but later on I should only change
# it when the min is bigger than number
# in the loop below how can i understand it is first iteration
count_of_iterations = 0
max = 0
for i in s:
    if count_of_iterations == 0:
        min = i
    if i < min:
        # if code comes to this line it means min is bigger than number
        min = i
    elif i > max1:
        max1 = i
    count_of_iterations +=1
print(min)
print(max1)

for i in s2:
    if max == 0:
        max = i
    if i > max:
        max = i
print(max)        

print(f"Multiplication of {min} + {max} = {min * max}")

