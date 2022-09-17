

list = ["Python","C++","C#","Java","Ruby"]

# Remove C# from the list

list.remove("C#") #'Python', 'C++', 'Java', 'Ruby'
print(list)

# i want to remove second element from this list

list.pop(1)
print(list) # 'Python', 'Java', 'Ruby'

# since -5 is not in the list it will give index out of range error
#list.pop(-5)
# Index out of range error
#list.pop(12)

# If you use bigger or lower indexes to get elements from iterable objects you will get index out of range error

nums = [1,2,3,5,4,5,6,7]

# it will remove the first 5 that exist in the list.
nums.remove(5)
print(nums)

nums.clear()
print(nums)









