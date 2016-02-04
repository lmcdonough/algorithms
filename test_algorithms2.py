
import random

def stock_prices():

	mylist = [random.randint(1, 100) for x in range(100)]

	max_profit = mylist[1] - mylist[0]
	max_num = mylist[0]

	for num in mylist:
		max_num = max(max_num, num)
		max_profit = max(max_profit, max_num - num)

	return max_profit

