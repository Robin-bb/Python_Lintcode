# Description
# Link:
# https://www.lintcode.com/problem/2407/
# In this question, we will provide an integer int_1, we have already declared the calculate_sum function for you in solution.py. The initial int_1 of this function represents the initial value, and you need to calculate the form a + aa + aaa + aaaa value, and finally print the result.

# Example
# The evaluation machine will execute your code by executing python main.py {input_path}, and the test data will be placed in the file corresponding to input_path. You can see how the code works in main.py.

# Example one

# When the input value is:

# 5
# The print result is:

# 6170
# Example two

# When the input value is:

# 9
# The print result is:

# 11106

# Solution:
def calculate_sum(int_1: int) -> None:
    """
    :param int_1: Input number
    :return: None
    """
    # -- write your code here --
    a = int_1
    aa = int_1 * 10 + int_1
    aaa = int_1 * 100 + int_1 * 10 + int_1
    aaaa = int_1 * 1000 + int_1 * 100 + int_1 * 10 + int_1
    print(a + aa + aaa + aaaa)

  
