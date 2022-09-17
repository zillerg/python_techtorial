s = set()

print(type(s))
print(s)
s.add("new value")

print(s)

s = {} # dict
print(type(s))

# using set() function we can convert lists into set

list = ["s","s",2,2,4,5,7,3,6,2,3]

set1 = set(list)
print(set1)

# clear()
set1.clear()

print(set1)

# copy method
list = ["s","s",2,2,4,5,7,3,6,2,3]

set1 = set(list)
print("From line 28th",set1)

set2 = set1.copy()
print(set1 == set2)
print("Set2 from line 31",set2)

