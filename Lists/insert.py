
# 

list = [11,7,44,6,8]

# insert number 9 on the index number 4

list.insert(4,9) #[11, 7, 44, 6, 9, 8]
print(list)

# insert method will take two parameters first is for index number
# second one is for the value of new element.
list.append(33)
print(list) #[11,7,44,6,9,8,33]

# if you provide bigger index than you have it will insert new element at the end of the list
list.insert(10,"new element")
print(list)
#This will create an exception.
#number of arguments for append is exactly 1
#list.append(4,90)

items = [2,3,4,5]

items.insert(2,1)
print(items)






