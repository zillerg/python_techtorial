
# Ask user to enter a date in format of month/day/year
#                                         mm/dd/yyyy
# Convert given date like following examples
# 03/06/2017                -> March 6, 2017
#   

# 07/10/2022            -> July 10, 2022


date = input()
# First two charachters of the given date will give you the number of month
month = date[0:2]
day   = date[3:5]
year  = date[-4:]
# In which conditions should I modify the date? 
# When the date is starting with 0, I should remove the 0
day = day.removeprefix("0")

if month == "01":
    print(f"January {day}, {year}")
elif month == "02":
     print(f"February {day}, {year}")
elif month == "03":
     print(f"March {day}, {year}")
elif month == "04":
     print(f"April {day}, {year}")
elif month == "05":
     print(f"May {day}, {year}")
elif month == "06":
     print(f"June {day}, {year}")
elif month == "07":
     print(f"July {day}, {year}")
elif month == "08":
     print(f"August {day}, {year}")
elif month == "09":
     print(f"September {day}, {year}")
elif month == "10":
     print(f"October {day}, {year}")
elif month == "11":
     print(f"November {day}, {year}")
elif month == "12":
     print(f"December {day}, {year}")



# if date[0:2] == "01":
#     print(date.replace("01","January"))
# elif date[0:2] == "02":
#     print(date.replace("02","February"))     
# elif date[0:2] == "03":
#     print(date.replace("03","March"))  
# elif date[0:2] == "04":
#     print(date.replace("04","April"))  
# elif date[0:2] == "05":
#     print(date.replace("05","May")) 
# elif date[0:2] == "06":
#     print(date.replace("06","June")) 
# elif date[0:2] == "07":
#     print(date.replace("07","July")) 
# elif date[0:2] == "08":
#     print(date.replace("08","August")) 
# elif date[0:2] == "09":
#     print(date.replace("09","September")) 
# elif date[0:2] == "10":
#     print(date.replace("10","October")) 
# elif date[0:2] == "11":
#     print(date.replace("11","November")) 
# elif date[0:2] == "12":
#     print(date.replace("12","December")) 