
import random

def stock_prices():

	mylist = [random.randint(1, 100) for x in range(100)]

	max_profit = mylist[1] - mylist[0]
	max_num = mylist[0]

	for num in mylist:
		max_num = max(max_num, num)
		max_profit = max(max_profit, max_num - num)

	return max_profit


def products():

	mylist = [1, 2, 3, 4, 5]
	new_list = []

	for index, num in enumerate(mylist):
		new_list.append(reduce(lambda x, y: x*y, [x for i, x in enumerate(mylist) if i != index]))

	return new_list


def condense_meetings():
	times = [(0, 1 ), (3, 5), (4, 8), (10, 12), (9, 10)]
	times.sort()
	meetings = []
	temp_start, temp_finish = times[0]
	
	for start, finish in times[1:]:
		if start <= temp_finish:
			temp_finish = max(temp_finish, finish)
		else:
			meetings.append((temp_start, temp_finish))
			temp_start, temp_finish = start, finish
	meetings.append((temp_start, temp_finish))
	return meetings


def parentheticals():
	string = "Sometimes (when I {nest them }(my parentheticals) [(too much)] (like this (and this))) they get confusing."

	paren_stack = []
	openers = '[({'
	closers = '])}'

	for char in string:
		if char in openers:
			paren_stack.append(char)
		elif char in closers:
			if not paren_stack or openers.index(paren_stack.pop()) != closers.index(char):
				return False

	return True


def palendrome():
	test_word = 'racecar'

	i = -1
	for index, char in enumerate(test_word):
		if index == abs(i - 1):
			return True
		elif char != test_word[i]:
			return False
		i -= i

def fibonacci(n):
	x, y = 0, 1

	for num in xrange(n):
		x, y = y, x+y
		print x


def primes(n):

	pass









