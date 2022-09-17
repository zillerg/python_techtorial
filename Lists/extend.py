
# 
need = ["pencil","eraser","notebook"]

need2 = ["computer","mouse","keyboard","camera"]

need.extend(need2)
print(need)

# What happens if you extend line with string
str = "Techtorial"
list = [1,2,3,4,5]

list.extend(str)
print(list)
#[1, 2, 3, 4, 5, 'T', 'e', 'c', 'h', 't', 'o', 'r', 'i', 'a', 'l']
# extend method only works with iterable object.

#list.extend(1234) # it will create an error

