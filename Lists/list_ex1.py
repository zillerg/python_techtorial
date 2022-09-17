

nums = [1,2,3,1,2,3,4,2,2]
#Remove all number 2's from this list.
# First I can find count of 2's in the list
# I can apply the remove methdo count times.

count = 0

for number in nums:
    if number == 2:
        count += 1
print(count)
# I need to apply the remove method count times
# I need to create a loop that iterates count times
#if the count is 5

# it will get executed count times
for i in range(count):
    nums.remove(2)
print(nums)








nums = [1,2,3,1,2,3,4,2,2]
#Remove all number 2's from this list.
# Create a copy of this list
newList = nums.copy()

for number in newList:
    if number == 2:
        nums.remove(number)


print(nums)

while count > len(nums):
    nums.remove(2)
print(nums)



