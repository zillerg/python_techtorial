
# Ask user to give two string values and print True 
# if the second string startswith last two chars
# of the first string OR print True 
# if the first string startswith first two chars of the second string

print("Enter first string:")
s1 = input()
print("Enter second string:")
s2 = input()

last_two_ch_1 = s1[-2:]

is_second_start = s2.startswith(last_two_ch_1)

first_two_ch_s2 = s2[:2]

is_first_start = s1.startswith(first_two_ch_s2)

print(is_second_start or is_first_start)