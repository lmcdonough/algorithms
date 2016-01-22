import random
import itertools


def stock_profit(prices):
	'''Takes a list of stock prices and returns the highest profit or minimum
	loss that can be achieved from said prices. It assumes the indices of the list 
	are time in minutes, for example prices[0] is the opening price. The complexity of
	this function is O(n) time and O(1) space because we only loop through the list once.'''

	lowest_price = prices[0]
	max_profit = prices[0] - prices[1]

	for price in prices:
		lowest_price = min(lowest_price, price)
		max_profit = max(max_profit, price - lowest_price)
	return max_profit



def get_products(lst):
	'''Takes a list of integers as input and returns a new list of products of every integer in the 
	list except the integer at that index. Below are two algorithms both of which have a complexity of 
	O(n) time and O(n) space. We make two passes through the input list and the list we build always
	has the same length as the input list.'''

	new_list = []
	for index, val in enumerate(lst):
		new_list.append(reduce(lambda x,y: x*y, [val for ind, val in enumerate(lst) if ind != index]))

	#below could also work
	new_list = [reduce(lambda x,y: x*y, lst[1:]),]
	temp_product = lst[0]
	for index, val in enumerate(lst[1:]):
		remaining_product = reduce(lambda x,y: x*y, [x for x in lst[index:]])
		new_list.append(temp_product*remaining_product)
		temp_product *= val



def highest_product(lst):
	'''Takes a list of integers as input and returns the highest possible product of
	three of the integers in the list. The complexity of the algorithm is O(n) time and 
	O(1) space.'''

	if len(lst) < 3:
		raise Exception('Less than 3 values in list.')

	highest_product_of_three = lst[0]*lst[1]*lst[2]
	highest_product_of_two = lst[0]*lst[1]
	lowest_product_of_two = lst[0]*lst[1]
	highest_num = lst[0]
	lowest_num = lst[0]

	for num in lst[2:]:
		highest_num = max(highest_num, num)
		lowest_num = min(lowest_num, num)
		highest_product_of_two = max(highest_product_of_two, highest_num * num, lowest_num * num)
		lowest_product_of_two = min(lowest_product_of_two, highest_num * num, lowest_num * num)
		highest_product_of_three = max(highest_product_of_three, highest_product_of_two*num, lowest_product_of_two*num)
	return highest_product_of_three



times = [(0,1),(3,5),(4,8),(10,12),(9,10)]

def condense_meetings(times):
	'''Takes a list of 2 integer tuples as input. The inputs represent a meeting start time,
	and end time. They are represented as the 30 minute blocks passed 9:00am. This condenses 
	all the meetings and returns a new schedule in the same format
	to show when everyone is available. The complexity is O(n lg n) time and (n) space. If the incoming list
	was already sorted it would be possible to reduce the runtime to O(n) time.'''

	times = sorted(times)
	new_meeting_times = []
	previous_meeting_start, previous_meeting_end = times[0]
	for start_time, end_time in times[1:]:
		if start_time <= previous_meeting_end:
			previous_meeting_end = max(previous_meeting_end, end_time)
		else:
			new_meeting_times.append((previous_meeting_start, previous_meeting_end))
			previous_meeting_start = start_time
			previous_meeting_end = end_time
	new_meeting_times.append((previous_meeting_start, previous_meeting_end))
	return new_meeting_times




string = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."


def parentheticals(string, paren):
	'''Takes a string, and index of an opening parenthesis. This then returns 
	the index of the corresponding closing parenthesis. Using the example above and the opening
	parenthesis index of 10, this would return 79. The complexity is O(n) time and O(1) space where 
	n is the length of the string.'''

	open_parens = 0
	
	for index, char in enumerate(string[paren:]):
		if char == '(':
			open_parens += 1
		if char == ')':
			open_parens -= 1
		if open_parens == 0:
			return paren+index



def palendrome(string):
	'''Takes a string as input and returns True if the string is a palendrome. The complexity
	is O(n) time and O(1) space.'''

	end_num = len(string) - 1
	palendrome = True
	for index, char in enumerate(string):
		if char != string[end_num]:
			palendrome = False
		if end_num == index:
			return palendrome
		end_num -= 1



def count_sort_chars(path):
	'''Takes a path to a file as input. This reads the file, and returns a dict of each letter with 
	their corresponding counts in the text. The dict is sorted in descending order by count. If there
	is a tie, they are then sorted alphabetically.'''

	with open(path) as f:
		lines = f.readlines()
		char_counts = {}

		for char in lines:
			if not char in char_counts:
				char_counts[char] = 1
			else:
				char_counts[char] += 1
		sort_chars = sorted(char_counts.iteritems(), key=lambda tup: (-tup[1], tup[0]))
		return sort_chars



class TempTracker(object):
	'''An interface to input and track temperatures. This allows for insertion of temps,
	and also has methods to return the min, max, mean, and mode temperatures seen so far. This class favors
	the speed of the getter methods over the insert method.'''

	def __init__(self):
		self.max_temp = None
		self.min_temp = None
		self.mean = None
		self.mode = None
		self.total = None
		self.temp_counts = {}
		self.max_count = None

	def insert(self, temp):
		self.max_temp = max(self.max_temp, temp)
		self.min_temp = min(self.min_temp, temp)
		self.total += temp
		self.mean = self.total / float(2)
		self.temp_counts[temp] += 1
		if self.temp_counts[temp] > self.max_count:
			self.max_count = self.temp_counts[temp]
			self.mode = temp
		

	def get_max(self):
		return self.max_temp

	def get_min(self):
		return self.min_temp

	def get_mean(self):
		return self.mean

	def get_mode(self):
		return self.mode


def fibonaccii(val):
	'''A simple function that takes an integer as input and returns a generator object. 
	The object will iterate over fibonaccii numbers until it reaches you input integer.'''

	final_num = 0
	for num in xrange(1,val):
		final_num += num
        yield final_num


bracket_string = '(()){}[()]'

def brackets_stack(bracket_string):
	'''Takes a string composed of parens and brackets. It then mimics a stack to 
	identify whether or not the string of parens and brackets are balanced.'''

	brackets = []
	opens = '([{'
	close = ')]}'
    
	for char in bracket_string:
		if char in opens:
			brackets.append(opens.index(char))
		elif char in close:
			if not brackets:
				return False
			elif brackets[-1] == close.index(char):
				brackets.pop()
			else:
				return False
	else:
		return True

        
def get_permutations(string):
    '''A recursive function that takes a string as input and returns a set of all possible permutations
    of that string.'''

    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    permutations_of_all_chars_except_last = get_permutations(all_chars_except_last)
    possible_positions_to_put_last_char = range(len(all_chars_except_last)+1)
    permutations = set()

    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in possible_positions_to_put_last_char:
            permutation = permutation_of_all_chars_except_last[:position] + last_char + permutation_of_all_chars_except_last[position:]
            print permutation
            permutations.add(permutation)

    return permutations


def fact_lim(n, lim):
	'''Takes two positive integers as input.
	Returns the sum of the factorials of all numbers starting 
	from n and ending at n - lim from 1 to n.'''

	error_message = 'Values are not positive integers.'
	
	if type(n) != int != type(lim):
		return error_message
	
	if n <= 0 or lim <= 0:
		return error_message

	total = []
	for i in xrange(n, 0, -1):
		product = i
		for index, num in enumerate(xrange(i, 0, -1)):
			if any([index >= lim-1, num == 1]):
				total.append(product)
				break
			product *= (num - 1)
	return sum(total)


def find_dupe(lst):
	'''The below function returns any integer that appears more than once in our list.
	The time complexity of the method is O(n log n)'''

	mylist = sorted(lst)
	dupe_dict = {}
	dupes = []
	
	for index, val in enumerate(mylist[:-1]):
		if val == mylist[index+1]:
			dupes.append(val)
	return list(set(dupes))

	#or you could do it using a dictionary
	for val in mylist:
		if val in dupe_dict:
			if dupe_dict[val] == 1:
				dupe_dict.pop(val, None)
			else:
				dupe_dict[val] -=1
		else:
			dupe_dict[val] = 1
	return dupe_dict



def sum_of_ints(lst_of_ints, sum_of_2):
	'''The below function takes an integer sum_of_2
	and a list of integers (lst_of_ints) and returns a 
	boolean indicating whether there are two numbers in 
	lst_of_ints whose sum equals sum_of_2. Both 
	solutions have a time complexity of O(n).'''

	# You could use itertools
	combos = itertools.combinations(lst_of_ints, 2)
	for int_one, int_two in combos:
		if int_one + int_two == sum_of_2:
			return True, int_one, int_two
	else:
		return False

	# or you could use a set and simple subtraction.
	ints_so_far = set()

	for int_one in sum_of_2:
		matching_int_2 = sum_of_2 - int_one
		if matching_int_2 in ints_so_far:
			return True
		ints_so_far.add(int_one)
	else:
		return False



def rectangle_intersections():

	my_rectangle = {
		'x': 1,
		'y': 5,
		'width': 10,
		'height': 4
	}

	my_rectangle2 = {
		'x': 4,
		'y': 7,
		'width': 3,
		'height': 11,
	}



	if my_rectangle['x'] < my_rectangle2['x']:
		x_intersects = range(my_rectangle2['x'], min(my_rectangle['x']+my_rectangle['width']+1, my_rectangle2['x']+my_rectangle2['width']+1))
	else:
		x_intersects = range(my_rectangle['x'], min(my_rectangle2['x']+my_rectangle2['width']+1, my_rectangle['x']+my_rectangle['width']+1))

	if my_rectangle['y'] < my_rectangle2['y']:
		y_intersects = range(my_rectangle2['y'], min(my_rectangle['y']+my_rectangle['height']+1, my_rectangle2['y']+my_rectangle2['height']+1))
	else:
		y_intersects = range(my_rectangle['y'], min(my_rectangle2['y']+my_rectangle2['height']+1, my_rectangle['y']+my_rectangle['height']+1))


	inter_dict2 = {'x': min(x_intersects), 'y': min(y_intersects), 'width': len(x_intersects), 'height': len(y_intersects)}


	rec1 = []
	for num in xrange(my_rectangle['x'], my_rectangle['width'] + my_rectangle['x'] + 1):
		for num2 in xrange(my_rectangle['y'], my_rectangle['height'] + my_rectangle['y'] + 1):
			rec1.append((num, num2))

	rec2 = []
	for num in xrange(my_rectangle2['x'], my_rectangle2['width'] + my_rectangle2['x'] + 1):
		for num2 in xrange(my_rectangle2['y'], my_rectangle2['height'] + my_rectangle2['y'] + 1):
			rec2.append((num, num2))	

	rec_set = set(rec1) & set(rec2)
	inter_rect = {}

	inter_rect['x'] = min(rec_set, key=lambda x: x[0])[0]
	inter_rect['y'] = min(rec_set, key=lambda x: x[1])[1]
	inter_rect['width'] = max(rec_set, key=lambda x: x[0])[0] - min(rec_set, key=lambda x: x[0])[0] + 1
	inter_rect['height'] = max(rec_set, key=lambda x: x[1])[1] - min(rec_set, key=lambda x: x[1])[1] + 1

	print 'recdict: {}\n\ninterdict: {}'.format(inter_rect, inter_dict2)









