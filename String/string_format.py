
number_of_students = 36

str ="Total number of student is {}" 
print(str.format(number_of_students))


number_of_teachers = 12

# create a string that shows number of teachers and 
# number of students

s = "The total number of teachers is {} and the total number of students is {}"
print(s.format(number_of_teachers, number_of_students))

# 

s = "The total number of teachers is {1} and the total number of students is {0}"
print(s.format(number_of_students, number_of_teachers))


s = f"Total number of teachers is {number_of_teachers}"
print(s)