

# Let's ask user a one string and remove the spaces in the 
# beginning and end of the string

print("Enter a text")
s = input()

s = s.strip()

print(s)


s = "           Python is a programmin language "
print(s.strip())

# In strip method we can provide a charachter and it will remove
# a certain charachter if that char is in 
# the beginning of the string.

# Let's write a phone number in the middle of the # tags
phone_number = "###7773332222##"
print(phone_number.strip("#"))

#Strip method can also work with multiple chars
# we can specify chars instead of removing the default space

web_site = "www.techtorial.com"
#get the domain name from this website
# .wcmo
print("Domain name of the website is",web_site.strip(".wcmo"))

# given a gmail address from user, print only the user's
# mail name
# For ex: example@gmail.com -> example
#         yct@gmail.com -> yct

print("Please enter your gmail")
gmail = input()
gmail_name = gmail.strip("@gmail.co")
print(gmail_name)

# rstrip method which allows us to just 
# remove trailing part of the string

gmail_name = gmail.rstrip("@gmail.co")
print(gmail_name)

# lstrip method which allows us to just 
# remove leading part of the string

#From the given website below, print only domain name and .com
web_site = "www.techtorial.com"

print(web_site.lstrip("www."))

# In the strip method we can easily mistaken, so
# we have to make sure and double check which part it is going to be removed