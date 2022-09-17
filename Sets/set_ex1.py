
a = [1,2,3,4,5]
b = [5,6,7,8,9]

s1 = set(a)
s2 = set(b)

# How can i check if there's common
#In the below i get common elements from both sets
common_elements = (s1.intersection(s2))

# if theres at least one common element what should be the size of common_elements set?
# It should be at least 1.
# len(common_elements) >= 1
# if len(common_elements) >= 1:
#     print("True")
# else:
#     print("False")

is_there_common = len(common_elements) >= 1
print(is_there_common)



