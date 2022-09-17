
# getting ticket for speed violation
#   in state of IN, speed limit on HighWays is 70
#   in other states, speed limit on Highways is 55
#   -if driver exceeds speed limit for up to 10% of the limit in each state, 
#    we will give WARNING in that state
#     state of IN warning means --> print --> "YELLOW WARNING"

#     other state warnings mean --> print --> "CITATION"
# -if driver exceeds speed limit more than 10% of the limit in each state,
#  we will give TICKET in that state
#     state of IN ticket means --> print --> "$150 and 5 points"
#     other state warnings mean --> print --> "$100"
# -if speed is same as  speed limit, --> print --> "You are driving safe!"

speed_limit_IN, speed_limit_other_states = 70, 55
print("What speed are you traveling at the moment?")
speed_of_driver = int(input())

print("What state are you in at the moment? ")
state_in = input()

# if the condition below is true driver is in indiana
# If the driver is not in IN the condition below will be False
is_in_IN = state_in == "Indiana" or "IN"

ten_percent_up_IN = speed_limit_IN + speed_limit_IN * 10 / 100
ten_percent_up_others = speed_limit_other_states + speed_limit_other_states * 10 / 100

if is_in_IN and speed_of_driver  <= speed_limit_IN:
    print("You are driving safe!")
elif is_in_IN and speed_of_driver > speed_limit_IN and speed_of_driver <= ten_percent_up_IN:
    print("Yellow Warning")
elif is_in_IN and speed_of_driver > ten_percent_up_IN:
    print("$150 and 5 points")
elif not is_in_IN and speed_of_driver <= speed_limit_other_states:
    print("You are driving safe!")
elif not is_in_IN and speed_of_driver > speed_limit_other_states and speed_of_driver <= ten_percent_up_others:
    print("CITATION")
elif not is_in_IN and speed_of_driver > ten_percent_up_others:
    print("$100")