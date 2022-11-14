# Description
# Get the input variable a and the variable b with input and you need to print the results of a and b logical operations separately in the IDE.
# Please print the results in the order of and, or, not.
# (When using not, please print the two variables separately)

# Example
# The evaluator will execute your code by executing the command python main.py with a, b as standard input from the console, on a separate line for each argument. Please print them in order.
# Example one.
# Variable a is True, variable b is False
# You need to output

# False
# True
# False
# True
# Example 2.
# Variable a is False, variable b is False
# You need to output

# False
# False
# True
# True

#Solution:
# read data from console
a = eval(input())
b = eval(input())
# write your code here
print(a and b)
print(a or b)
print(not a)
print(not b)


