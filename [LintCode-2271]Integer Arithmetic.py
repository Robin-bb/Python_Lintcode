# Description
# Link:
# https://www.lintcode.com/problem/2271/
# Please get two integers a, b from the standard input stream (console), and calculate the sum, difference, product and quotient of a, b. (The quotient only keeps the integer part). Then output to the standard output stream (console) through the print statement. The results are divided into four lines for output.
# 100001≤a,b≤10000
# Example
# The evaluation opportunity executes your code by executing the command python main.py. Your code needs to read data a, b from the standard input stream (console), and add the sum, difference, product, and quotient of a, b. (The quotient only keeps the integer part) is printed in four lines to the standard output stream (console).

# Example 1

# When a = 9 and b = 6, the printed result of the program execution is:
# 15
# 3
# 54
# 1
# Explanation:

# a + b = 15a+b=15

# a-b = 3a−b=3

# a \times b = 54a×b=54

# \lfloor a \div b \rfloor = 1⌊a÷b⌋=1

# Example 2

# When a = 5 and b = 10, the printed result of the program execution is:
#   15
# -5
# 50
# 0
# Explanation:

# a + b = 15a+b=15

# a-b = -5a−b=−5

# a \times b = 50a×b=50

# \lfloor a \div b \rfloor = 0⌊a÷b⌋=0

# Solution:
# write your code here
# read data from console
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)
print(a // b)

# output the answer to the console according to the requirements of the question

