# Description
# This problem has a list list_1. We need you to refine the code in solution.py to do the following.

# modify the element in the third position of the index of the list list_1 to be 1999.
# add an element 'jiuzhang' to the list list_1.
# delete the first element of the list list_1.
# We will import the code you refined in solution.py in main.py and run it. If your code is logically correct and runs successfully, the program will output list_1 with the changed elements.ents.


# Example
# The evaluation machine will execute your code by executing python main.py {input_path} and the test data will be placed in the file corresponding to input_path. You can see how the code is run in main.py.

# Example 1.

# If the following parameters are passed in.

# list_1 = ['python', 'Rico', 2000]
# The result obtained is.

# ['Rico', 1999, 'jiuzhang']
# Sample two.

# If the following parameters are passed.

# list_1 = ['python', 'Ron', 2018]
# The result obtained is.

# ['Ron', 1999, 'jiuzhang']
# ```1999, 'jiuzhang']

# Solution:

def list_update_del(list_1: list) -> list:
    """
    :param list_1:  the source list
    :return: modified list_1
    """
    # --write your code here--
    list_1[2] = 1999
    list_1.append("jiuzhang")
    list_1.pop(0)
    return list_1
  
  
