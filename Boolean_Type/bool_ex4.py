
# Create a program to print True if there is enough tickets for the nba game
# We will have 2 variables sold tickets and max capacity of the stadiumm
# If stadium capacity is more than sold tickets we should print True and all other case 
# we should print False

sold_tickets, max_capacity = 6000, 5000
tickets_left = max_capacity - sold_tickets
if tickets_left < 0:
    print("Too many tickets were sold:",tickets_left)
else:    
    print("tickets left",tickets_left)
is_enough_space_available = max_capacity > sold_tickets
print("Is there enough space at NBA game:",is_enough_space_available)
