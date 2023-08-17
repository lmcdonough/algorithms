from count_sort_chars import count_sort_char


class TestCountSortChar:
    # Tests that the function can handle a file containing only one character
    def test_single_char_file(self):
        assert count_sort_char('test_files/single_char.txt') == [('a', 1)]

    # Tests that the function can handle a file containing multiple characters
    def test_multi_char_file(self):
        assert count_sort_char('test_files/multi_char.txt') == [('a', 2), ('b', 2), ('c', 3)]

    # Tests that the function can handle a file containing special characters
    def test_special_char_file(self):
        assert count_sort_char('test_files/special_char.txt') == [('!', 1), ('#', 1), ('$', 1), ('%', 1), ('&', 1), ('*', 1), ('+', 1), ('-', 1), ('/', 1), ('<', 1), ('=', 1), ('>', 1), ('?', 1), ('@', 1), ('^', 1), ('_', 1)]

    # Tests that the function can handle a file containing numbers
    def test_number_file(self):
        assert count_sort_char('test_files/number.txt') == [('0', 1), ('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1), ('7', 1), ('8', 1), ('9', 1)]

    # Tests that the function can handle an empty file
    def test_empty_file(self):
        assert count_sort_char('test_files/empty.txt') == []

    # Tests that the function can handle a file containing only whitespaces
    def test_whitespace_file(self):
        assert count_sort_char('test_files/whitespace.txt') == [(' ', 5), ('\n', 2)]
