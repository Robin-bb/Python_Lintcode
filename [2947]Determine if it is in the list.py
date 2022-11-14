# Description
# Given a number num_1 and a list list_1, add num_1 to the square of num_1 and divide exactly by num_1 + 2, then determine if the number is in the list list_1 and print out the result.
# Example
# The evaluator will execute your program with python main.py {input_data}. The number num_1, and the list list_1 are given, and you are asked to process this number, then determine if the resulting number is in the list list_1, and print the result.
# Example 1.
# Input.

# num_1 = 3
# list_1 = [2, 4, 5, 1]
# Output.

# True
# Explanation.
# (3+3^2) \div(3+2) = 2(3+3 
# 2
#  )÷(3+2)=2
# 2 in the list [2,4,5,1], so print True
# Sample 2.
# Input.

# num_1 = 8
# list_1 = [5, 3, 8, 0, 10]
# Output.

# False
# Explanation.
# (8+8^2) \div(8+2) = 7(8+8 
# 2
#  )÷(8+2)=7
# 7 is not in the list [5, 3, 8, 0, 10], so it prints False

#Solution:
  
import sys
import math

# Get the num, list
num_1 = int(sys.argv[1])
list_1 = eval(sys.argv[2])
# please write your code here
# new_num = (num_1 + num_1*num_1) // (num_1 + 2)
# new_num = int((num_1 + num_1 * num_1) / (num_1 + 2))
new_num = int((num_1 + math.pow(num_1, 2)) / (num_1 + 2))
# print(new_num)
# print(list_1)
if new_num in list_1:
    print(True)
else:
    print(False)
