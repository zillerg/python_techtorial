
str = "regularly"
# print true if this string ends with ly

print(str.endswith("ly"))
# True
print(str.startswith("r"))
# True
print(str.endswith("yl"))
# False
print(str.startswith("er"))
# False
print(str.startswith("regularly"))
# True
print(str.endswith("regularly"))
# True
print(str.startswith("eg"))
# False
print(str.endswith("LY"))
# False bc case sensative
print(str.startswith("RE"))
# False