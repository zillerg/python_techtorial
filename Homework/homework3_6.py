

print("Enter one string value")
str = input()
s = str.strip()
string = ""

for i in s:
    if i.upper() == i:
        string += " "+ i
    else:
        string += i
print(string.strip())    
        


