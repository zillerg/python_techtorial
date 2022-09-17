
# tuples are immutable so we can't change it and it doesn't have methods


fruits = ("strawberry", "apple", "orange", "banana")

print(fruits)
print(type(fruits))

print(fruits.index("apple"))   # -> we will get 1 the index

print(fruits.count("orange"))


# Accessing elements in the tuple
# we can use index numbers as we did with list

# print(fruits[2]) # "orange"

# for element in fruits:
#     print(element)


# fruits = ("strawberry", "apple", "orange", "banana")
# from this tuple print out first fruit name that has odd length. if there's no fruit with odd length 
# print odd length couldn't be found.
odd_fruit = ""

for i in fruits:
    if len(i) % 2 != 0:
        # i have found odd length
        odd_fruit = i
        break   
if odd_fruit != "":
    print("First odd fruit is", odd_fruit)
else:
    print("Odd length fruit is not found")


