
bool1 = True
bool2 = False
bool3 = True
#not operator will make true condition false and false conditions true.
print(not bool3) #False
print(not bool2) #True

print(bool2 and bool1) # Since and condition requires both sides to be true for return
#this line will print False.

print(bool2 or bool1) #If one of conditions is True, or will return True.
        #False    False
print(bool2 or not bool1) # It will return False bc not operator will
# make the bool1 value false so False will result in false
        #True       True
print(not bool2 and bool1) # It will return True bc not operator will make the bool2 True
