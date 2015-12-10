import random


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



def product_problem_redo(lst):
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


def sort_multiple(string):
	'''Take a string in descending order by occurance of chars then ascending alphabetically.'''
	counts = {}
	for letter in string:
		if not letter in counts:
			counts[letter] = 1
		else:
			counts[letter] += 1
	return sorted(counts.iteritems(), key=lambda tup: (-tup[1], tup[0]))


def sort_multiple_redo(path):
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



#Temp Tracker
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










