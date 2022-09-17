

print("Enter a string")
str = input()
str = str.strip()
new_str = ""
# for i in range(1,len(str_noSpaces)+ 1):
#     new_str = str_noSpaces[len(str_noSpaces) - i ] 
#     print(new_str)  

# count = len(str_noSpaces)
# while count  > 0:
#     new_str += str_noSpaces[count - 1]
#     print(str_noSpaces[index])     
#     count -= 1

# for i in str_noSpaces:
#     new_str = new_str + i
#     print(i)
# print(new_str)    


for i in str:
    new_str = i + new_str
print(new_str)    

