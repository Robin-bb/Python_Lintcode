# Description
# There is a new item in the store and regular customers need to buy it at the original price, while members can enjoy 30% discount. If a customer is on the blacklist, then the store will not sell the item to him. There is a list of members, and a blacklist. A customer comes in and you print out the price that the customer will eventually have to pay. If the customer is on the blacklist, you need to print -1.
# Parameter Comments.

# Product price: price(int)
# Member list: vip(list)
# blacklist: blacklist(list)
# Customer: customer(str)

# Customers cannot be on both member list and blacklist at the same time

# Example
# The reviewer will execute your code via python main.py <{input_path}, where you need to determine the identity of the customer and then give the final price that needs to be paid.
# Sample example one.
# Input.

# price = 100
# customer = 'Jack'
# vip = ['coco', 'wowo', 'mick', 'Jack']
# black = ['Telang', 'pupu']
# Output.

# 70.00
# Sample II.
# Input.

# price = 899
# customer = 'DadaGuai'
# vip = ['coco', 'wowo', 'look', 'Jack']
# black = ['DadaGuai', 'pupu']
# Output.

# -1

#Solution:
# Get Variables
price = int(input())
customer = eval(input())
vip = eval(input())
blacklist = eval(input())
# please write your code here
if customer in vip:
    print(f'{price * 0.7 :0.2f}')
elif customer in blacklist:
    print(-1)
else:
    print(price)
