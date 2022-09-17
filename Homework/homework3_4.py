

print("Enter a number between 1 to 10")
num = int(input())

if num <= 10:
    for i in range(num,0, -1):
        print(str(i) * i)
else:
    print("Your number exceeds 10")     