# Add Two Numbers in Python
# Author: Jinyu Li (Leo)
# Using a function

# function
def add(a, b):
    sum = float(a) + float(b)
    return sum

# get input from user and convert them to float
a = input("[Enter the first number]\n")
b = input("[Enter the second number]\n")

# add them together
sum = add(a, b)

# print it out
print("[Answer]\n<%.0f>" % sum)
