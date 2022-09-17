
bool1 = True
bool2 = False
a     = 5
# The word True in boolean numerically represented by 1
# The word False in boolean numerically represented by 0
print(bool1+5) # 6
#print(True + a) #6
b = 2

print(bool2 * b) # 0 because since the value of bool2 is False and False is represented
# by 0 0*any number will give 0

text = "Text"
#Since the boolean values are not represented by text value we cannot 
# use +(Addition) symbol between string and boolean
#Therefore, following line will generate an error
#print(bool1+text)
#----------------------------------
print(bool1,text) # True Text

# We will only see numerical output with boolean
#  only when we use mathematical operation with other 
# numerical data types