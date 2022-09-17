

from curses.ascii import isupper


print("Enter one string value")
str = input()
s = str.strip()

str1 = ""
unique_ch = ""
for letter in s:
    if letter not in unique_ch :
        unique_ch += letter
 
print(unique_ch)












