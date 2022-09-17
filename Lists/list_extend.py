
need = ["pencil","eraser","notebook"]

need2 = ["computer","mouse","keyboard","camera"]


need.extend(need2)
# Extend method takes the copy of need2 list and adds it to the need list
# Later on changing the value of need2 will not effect the need
# bc when we are adding with extend method we didn't exactly
# use need2 we have used the copy of need2

need2.clear()
print(need)
#'pencil', 'eraser', 'notebook', 'computer', 'mouse', 'keyboard', 'camera'

print(need2) # empty list

















