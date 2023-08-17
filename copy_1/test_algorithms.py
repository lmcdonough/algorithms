from __future__ import print_function
import json, os, pprint
from random import randint
from collections import Counter, defaultdict
import itertools

def testing():
	mydict = {
		'a' : 'hello',
		'b' : [1, 2, 3],
		'c' : {
			3 : 4,
			2 : [1, 3, ['a', 'b', 'c']]
		},
		4 : 'what'
	}

	filename = os.path.join(os.getcwd(), 'myfile.json')
	with open(filename, 'w') as f:
		print('writing json file.')
		json.dump(mydict, f)


def read():
	filename = os.path.join(os.getcwd(), 'myfile.json')
	with open(filename) as f:
		print('retrieving json file.')
		return pprint.pprint(json.load(f))


def stock_profit():
	# mylist = [randint(0,100) for x in xrange(100)]
	mylist = [1, 5, 3, 1, 7, 8, 7]
	max_profit = mylist[0] - mylist[1]
	max_val = mylist[0]

	for val in mylist:
		max_val = max(max_val, val)
		max_profit = max(max_val - val, max_profit)

	return max_profit 	

def get_product():
	mylist = [1, 2, 3, 4, 5]
	mylist2 = []
	for index in xrange(len(mylist)):
		mylist2.append(reduce(lambda x, y: x*y, [x for i, x in enumerate(mylist) if not i == index]))

	return mylist2


def highest_possible_product():
	mylist = [1, 3, 5, 2, 7, 4, 5]
	highest_product_of_three = mylist[0]*mylist[1]*mylist[2]
	highest_product_of_two = mylist[0]*mylist[1]
	lowest_product_of_two = mylist[0]*mylist[1]
	highest_num = mylist[0]
	lowest_num = mylist[0]


	for val in mylist[3:]:
		highest_product_of_two = max(highest_num*val, lowest_num*val, highest_product_of_two)
		lowest_product_of_two = min(lowest_num*val, highest_num*val, lowest_product_of_two)
		highest_product_of_three = max(highest_product_of_three, highest_product_of_two*val, lowest_product_of_two*val)
		highest_num = max(highest_num, val)
		lowest_num = min(lowest_num, val)

	return highest_product_of_three


def condense_times():
	times = [(0,1),(3,5),(4,8),(10,12),(9,10)]
	times.sort()
	condensed_times = []
	previous_meeting_start, previous_meeting_end = times[0]

	for meeting_start, meeting_end in times[1:]:
		if meeting_start <= previous_meeting_end:
			previous_meeting_end = max(previous_meeting_end, meeting_end)
		else:
			condensed_times.append((previous_meeting_start, previous_meeting_end))
			previous_meeting_start = meeting_start
			previous_meeting_end = meeting_end
	condensed_times.append((previous_meeting_start, previous_meeting_end))
	return condensed_times


def balanced_parens():

	mystring = '(asfdsf)sf[(asdf)asdfsf]{sd(asdf)sdf}'
	paren_stack = []
	opening = '([{'
	closing = ')]}'

	for char in mystring:
		if char in opening:
			paren_stack.append(char)
		elif char in closing:
			if not opening.index(paren_stack.pop()) == closing.index(char):
				return False
	
	if paren_stack:
		return False
	else:
		return True


def palendrome():

	mystring = 'racecar'
	i = len(mystring) - 1

	for index, val in enumerate(mystring):
		if index == i:
			return True
		if not val == mystring[i]:
			return False
		i -= 1


def counts():
	filename = os.path.join(os.getcwd(), 'testfile.txt')
	with open(filename) as fp:
		test = ''.join(fp.read().splitlines()).replace(' ', '')	

	return sorted(Counter(test).items(), key=lambda tup: (-tup[1], tup[0]))

import string

def word_cloud():
	filename = 'testfile.txt'
	with open(os.path.join(os.getcwd(), filename)) as f:
		text = ''.join(f.read().splitlines()).lower()
	for c in string.punctuation:
		text = text.replace(c, '')
	text_dict = Counter(text.split())
	text_list = [(x, y) for x, y in text_dict.iteritems()]
	text_list.sort(key=lambda tup: -tup[1])

	return text_list



def find_dupes():
	mydict = defaultdict(int)
	mystring = 'sjaldhfhksksjdid'
	for val in mystring:
		mydict[val] += 1
		if mydict[val] > 1:
			print(val)
	return mydict


def sum_2(num):

	list_of_ints = [randint(1, 20) for x in xrange(10)]
	print(list_of_ints)
	combos = itertools.combinations(list_of_ints, 2)
	for val in combos:
		if val[0] + val[1] == num:
			return val
	return False


class A(object):

	def __init__(self):
		pass

	def __private(self):
		return 'hello'

class B(A):

	def __init__(self):
		pass

	def __private(self):
		return 'world'

	def test(self):
		return super(B, self)._A__private() + self.__private()

class C(A):

	def __init__(self):
		pass

	def __private(self):
		return 'test'



from collections import namedtuple

# make a basic Link class
Link = namedtuple('Link', ['id', 'submitter_id', 'submitted_time', 'votes',
                           'title', 'url'])

# list of Links to work with
links = [
    Link(0, 60398, 1334014208.0, 109,
         "C overtakes Java as the No. 1 programming language in the TIOBE index.",
         "http://pixelstech.net/article/index.php?id=1333969280"),
    Link(1, 60254, 1333962645.0, 891,
         "This explains why technical books are all ridiculously thick and overpriced",
         "http://prog21.dadgum.com/65.html"),
    Link(23, 62945, 1333894106.0, 351,
         "Learn Haskell Fast and Hard",
         "http://yannesposito.com/Scratch/en/blog/Haskell-the-Hard-Way/"),
    Link(2, 6084, 1333996166.0, 81,
         "Announcing Yesod 1.0- a robust, developer friendly, high performance web framework for Haskell",
         "http://www.yesodweb.com/blog/2012/04/announcing-yesod-1-0"),
    Link(3, 30305, 1333968061.0, 270,
         "TIL about the Lisp Curse",
         "http://www.winestockwebdesign.com/Essays/Lisp_Curse.html"),
    Link(4, 59008, 1334016506.0, 19,
         "The Downfall of Imperative Programming. Functional Programming and the Multicore Revolution",
         "http://fpcomplete.com/the-downfall-of-imperative-programming/"),
    Link(5, 8712, 1333993676.0, 26,
         "Open Source - Twitter Stock Market Game - ",
         "http://www.twitstreet.com/"),
    Link(6, 48626, 1333975127.0, 63,
         "First look: Qt 5 makes JavaScript a first-class citizen for app development",
         "http://arstechnica.com/business/news/2012/04/an-in-depth-look-at-qt-5-making-javascript-a-first-class-citizen-for-native-cross-platform-developme.ars"),
    Link(7, 30172, 1334017294.0, 5,
         "Benchmark of Dictionary Structures", "http://lh3lh3.users.sourceforge.net/udb.shtml"),
    Link(8, 678, 1334014446.0, 7,
         "If It's Not on Prod, It Doesn't Count: The Value of Frequent Releases",
         "http://bits.shutterstock.com/?p=165"),
    Link(9, 29168, 1334006443.0, 18,
         "Language proposal: dave",
         "http://davelang.github.com/"),
    Link(17, 48626, 1334020271.0, 1,
         "LispNYC and EmacsNYC meetup Tuesday Night: Large Scale Development with Elisp ",
         "http://www.meetup.com/LispNYC/events/47373722/"),
    Link(101, 62443, 1334018620.0, 4,
         "research!rsc: Zip Files All The Way Down",
         "http://research.swtch.com/zip"),
    Link(12, 10262, 1334018169.0, 5,
         "The Tyranny of the Diff",
         "http://michaelfeathers.typepad.com/michael_feathers_blog/2012/04/the-tyranny-of-the-diff.html"),
    Link(13, 20831, 1333996529.0, 14,
         "Understanding NIO.2 File Channels in Java 7",
         "http://java.dzone.com/articles/understanding-nio2-file"),
    Link(15, 62443, 1333900877.0, 1244,
         "Why vector icons don't work",
         "http://www.pushing-pixels.org/2011/11/04/about-those-vector-icons.html"),
    Link(14, 30650, 1334013659.0, 3,
         "Python - Getting Data Into Graphite - Code Examples",
         "http://coreygoldberg.blogspot.com/2012/04/python-getting-data-into-graphite-code.html"),
    Link(16, 15330, 1333985877.0, 9,
         "Mozilla: The Web as the Platform and The Kilimanjaro Event",
         "https://groups.google.com/forum/?fromgroups#!topic/mozilla.dev.planning/Y9v46wFeejA"),
    Link(18, 62443, 1333939389.0, 104,
         "github is making me feel stupid(er)",
         "http://www.serpentine.com/blog/2012/04/08/github-is-making-me-feel-stupider/"),
    Link(19, 6937, 1333949857.0, 39,
         "BitC Retrospective: The Issues with Type Classes",
         "http://www.bitc-lang.org/pipermail/bitc-dev/2012-April/003315.html"),
    Link(20, 51067, 1333974585.0, 14,
         "Object Oriented C: Class-like Structures",
         "http://cecilsunkure.blogspot.com/2012/04/object-oriented-c-class-like-structures.html"),
    Link(10, 23944, 1333943632.0, 188,
         "The LOVE game framework version 0.8.0 has been released - with GLSL shader support!",
         "https://love2d.org/forums/viewtopic.php?f=3&amp;t=8750"),
    Link(22, 39191, 1334005674.0, 11,
         "An open letter to language designers: Please kill your sacred cows. (megarant)",
         "http://joshondesign.com/2012/03/09/open-letter-language-designers"),
    Link(21, 3777, 1333996565.0, 2,
         "Developers guide to Garage48 hackatron",
         "http://martingryner.com/developers-guide-to-garage48-hackatron/"),
    Link(24, 48626, 1333934004.0, 17,
         "An R programmer looks at Julia",
         "http://www.r-bloggers.com/an-r-programmer-looks-at-julia/")]
         
         
def query():
    submitted_links = []
    for l in links:
        if l.submitter_id == 62443:
            if not submitted_links:
                submitted_links.append(l)
            else:
                i = 0
                import pdb; pdb.set_trace()
                while all([l.submitted_time < submitted_links[i].submitted_time, i < len(links)]):
                    i += i
                    print(l.id, submitted_links[i].id)
                submitted_links.insert(i, l)
    return submitted_links
                    




