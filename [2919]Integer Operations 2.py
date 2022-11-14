# Description
# Get two integers a, b from the standard input stream (console) and calculate the modulus of a over b, the bth power of a, and the integer division of a by b. Then output to the standard output stream (console) with the print statement. The result is split into three lines for output.

# Example
# Example 1

# When a = 9 and b = 2, the program execution prints out the result as

# 1
# 81
# 4
# Explanation.

# a \% b= 1a%b=1

# a ^ b = 81a 
# b
#  =81

# a \div b = 4a÷b=4

# Example 2

# When a = 8 and b = 3, the program execution prints out the result as

# 2
# 512
# 2
# Explanation.

# a \% b = 2a%b=2

# a ^ b = 512a 
# b
#  =512

# a \div b = 2a÷b=2

#Solution:

a = int(input())
b = int(input())
# output the answer to the console according to the requirements of the question
print(a % b)
print(a ** b)
print(a // b)


