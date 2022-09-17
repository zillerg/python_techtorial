
# There are some methods we can compare two sets with each other.

s1 = {1,7,9,3}

s2 = {2,7,9,5}
# returns unique elements from set1 which don't exist in set2
# difference method will get the elements present in set
# that is not present in the other set
print(s1.difference(s2)) # {1,3}

print(s2.difference(s1)) # {2,5}


# What do you think the return type of difference method?
print(type(s2.difference(s1))) # returns <class 'set'>

# Intersection method will return elements that are present in both sets.
print(s1.intersection(s2)) # {7,9}
print(type(s1.intersection(s2))) # <class 'set'>


#issubset() method
# it checks given set is present in the other set or not
set = {1,2,3,4,5}
set2 = {2,3,4}
# Since all elements of the set2 are in the set
# set2 is subset of the set.
print(set2.issubset(set)) # True
print(set.issubset(set2)) # False

# is superset()
# it checks if the set is superset of the given set.
# If the set has all the elements of the other set
# set is a superset of the set?
print(set.issuperset(set2)) # True
print(set2.issuperset(set)) # False



# Intersection_update
# It will remove all the elements that are not present in the other set
# Intersection_update doesn't return type.
s1 = {1,2,3}

s2 = {2,3}
s1.intersection_update(s2)
print(s1)

# difference_update
s1 = {1,2,3}

s2 = {2,3}
s1.difference_update(s2)
print(s1)

print(s2)

s3 = {1,2,3}
s2.difference_update(s3)

print(s2)



