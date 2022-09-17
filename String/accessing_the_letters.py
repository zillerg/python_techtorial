
day =  "Saturday"
#       01234567
letter5th = day[4]
print(day[4]) # r
print(type(letter5th)) # r

#What is the last index number of the day?
last_index = len(day) - 1
print("Last index is", last_index)

day2 = "Monday"
#If the last two or first two chars of the day and day2 is same print True

# What will be the index number for first two char in the string?
# It will always be 0 and 1

# What will be the index numbers for last two chars in the string?
#length of the stirng -1 and -2

first_two_chars_of_day = day[0] + day[1]
first_two_chars_of_day2 = day2[0] + day[1]
#condition will check if the first two chars of the string are the same or not
is_first2_same = first_two_chars_of_day == first_two_chars_of_day2

last_two_chars_of_day = day[len(day)-2]+ day[len(day)-1] 
last_two_chars_of_day2 = day2[len(day2)-2]+ day2[len(day2)-1] 

is_last_two_same = last_two_chars_of_day == last_two_chars_of_day2

condition = is_last_two_same or is_first2_same
print(condition)