

print("Enter a min number")
min = int(input())

print("Enter a max number")
max = int(input())
sum = 0
text = ""

for i in range(min, max+1):
    if i % 11 == 0 and i % 3 == 0:
        text = text + str(i) +  " + "
        sum += i
print(text.removesuffix(" + "),"=" , sum)            























