
#Write the code to check the student pass the class or not. 
# To be able to pass the class student need to have at least 65 score from 
# the exams and student need to attend the at least 80 percent of all the classes. 
# To calculate the average score we need to take take 20 percent of first exam score 
# and 30 percent of second exam score and 50 percent of third exam score. 
# We are given variables for three exam scores and one variable 
# for attendance to classes. If all conditions are met, 
# print true at the end. If not, print false.

exam1 = 60
exam2 = 40
exam3 = 90

attendancy = 80

avg_score = exam1*20/100 + exam2*30/100 + exam3*50/100 

is_attendancy_enough = attendancy >= 80

is_avg_score_enough = avg_score >= 65

can_pass = is_attendancy_enough and is_avg_score_enough

print("Average score of the student", avg_score)
print("Attendancy of the student", attendancy)
print("Student can pass the class",can_pass)
