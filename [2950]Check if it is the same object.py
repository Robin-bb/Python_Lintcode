#Description
#You are asked to define two variables num_1, num_2. Then do the following.

#assign num_1, num_2 both to 256. determine if num_1, num_2 are the same object.
#assign num_1, num_2 both to 257. determine if num_1, num_2 are the same object.
#assign num_1, num_2 both to -5. Determine if num_1, num_2 are the same object. 4. assign num_1, num_2 both to -5.
#Assign num_1, num_2 both to -6. Determine if num_1, num_2 are the same object.
#Enter the same code in the python interactive interface on your computer and see if the result is the same as the answer to this question. Please consult the relevant information and think about why this is the case.

#Example
#The evaluator will execute your code via python solution.py. There is no input to this problem, you just need to print the result on the console as required.
#Please consult the relevant information and think about why this is happening.
#Output.

#True
#True
#True
#True
#python interactive interface execution results.

#>>> num_1 = 256
#>>> num_2 = 256
#>>> num_1 is num_2 
#True
#>>> num_1 = 257
#>>>> num_2 = 257
#>>> num_1 is num_2 
#False
#>>>> num_1 = -5
#>>>> num_2 = -5
#>>> num_1 is num_2 
#True
#>>> num_1 = -6
#>>>> num_2 = -6
#>>> num_1 is num_2 
#False

#Solution:
# # Please write your code here
# num_1 = 256# this is an object
# num_2 = 256# this is another object
# print(num_1 == num_2)# compare if these 2 object is exactly the same
#                      # num_1 is a reference to the same object(reside in memory), num_1 is address to this memory location to this object()
#                      # num_2 is another reference to the same object
# #how to understand a variable
# a = a + 1 #(1)time-concept: right-part of assignment is always first, left-part is the latter
#           #(2)space-concept: a-variable is the bucket place to hold a type of value

num_1 = 256# this is an object
num_2 = 256# this is another object
print(num_1 == num_2)
num_1 = 257
num_2 = 257
print(num_1 == num_2)
num_1 = -5
num_2 = -5
print(num_1 == num_2)
num_1 = -6
num_2 = -6
print(num_1 == num_2)


