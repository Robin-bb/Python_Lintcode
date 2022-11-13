#LintCode 2267 · Find The Maximum Of Three Numbers

# link: https://www.lintcode.com/problem/2267/
# Give three positive integers a, b, c, get the maximum value by comparison, and output the maximum value of with print statement

# 1≤a,b,c≤10000

# Example
# The profiler will execute your code by Python main.py {a} {b} {c}

# Example 1:
# When a = 3, b = 7, c = 2, the results of the program execution printing are:
# 7
# Explanation:
# 7 is the largest number

# Example 2:
# When a = 2, b = 9, c = 4, the results of the program execution printing are:
# 9
# Explanation:
# 9 is the largest number


# solution-1: if-else compare
  
import sys

a = int(input())
b = int(input())
c = int(input())

#initialization
max_value = a

if (a > b):
    max_value = a
else: 
    max_value = b

if (max_value > c):
    max_value = max_value
else:
    max_value = c

print(max_value) 


# solution-2:
import sys

a = int(input())
b = int(input())
c = int(input())

max_value = 0

if a >= b and a >= c:
  max_value = a
if b >= a and b >= c:
  max_value = b
if c >= a and c >= b:
  max_value = c
  
print(max_value)  
  

# solution-3: use max() function
import sys

a = int(input())
b = int(input())
c = int(input())

max_value = max(a, b, c)

print(max_value)

