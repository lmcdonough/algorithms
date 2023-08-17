def count_sort_char(path):
    # create containers and/or cursors
    char_counts = {}

    # open file in default read mode
    with open(path) as f:
        # create list of chars from the file
        lines = f.readlines()

        # start iterating
        for char in lines:
            if char not in char_counts:  # the truth: char isnt in dict
                char_counts[char] = 1  # math: add char to dict with val
                # of 1
            else:  # the false: char is in dict
                char_counts[char] += 1  # math: increment the chars value
                # in the dict by 1

        # create a list of tuples from the key,val in the dictionary
        char_counts_list = char_counts.iteritems()  # looks like [("v": 4), ("b", 9), ("d": 7)] = jls_extract_def()

        # using the sorted function, sort the list of tuples using a lambda to evaluate/compare each iteam/tuple
        # the lambda sorts each tuple first in descending order of the second index, then if a tie, ascending by
        # the first index
        sort_chars = sorted(char_counts_list, key=lambda tup: (tup[-1], tup[0]))

    # returns the sorted list of tuples
    return sort_chars
