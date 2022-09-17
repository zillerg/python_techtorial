
# We use two methods to remove elements from the set.
# discard() meethod and remove() method.

# remove(valueOfTheObject)

set = {3,5,7,9}

# I want to remove the number 7 from the set.

set.remove(7)
# number 7 will be gone from the set.
print(set)

# When the element needs to be removed does not exist in the set.
# it will throw an error.
# set.remove(7)


# discard(valueOfObject) method 

set.discard(3)
print(set)
# When the element needs to be removed does not exist in the set.
# it will not throw an error and it won't do anything.
set.discard(3)



