

#Every math operation between float and int data type
# will result in float data type

floatNum = 3.0
intNum = 5
print("Type of floatNum is", type(floatNum))
print("Type of intNum is", type(intNum))

addition = floatNum + intNum
print("Addition of float and int is", type(addition))

subtraction = intNum - floatNum
print("Subtraction between int and float is", type(subtraction))

multiplication = floatNum * intNum
print("Multiplication between int and float is", type(multiplication))

division = intNum / floatNum
print("Division between float and int is",type(division))

remainder = floatNum % intNum
print("Remainder between float and int data type is", type(remainder))

#There is only one way to get int which is using //
int_division = floatNum // intNum
print("The Integer symbol divison result between float and int is", type(int_division))

square_of_float = floatNum * intNum
print(type(square_of_float))

