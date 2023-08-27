import unittest
from typing import List
from meetings import Meetings

class MeetingsTest(unittest.TestCase):
    def setUp(self):
        self.meetings = Meetings()

    def test_merge_intervals(self):
        meetings = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected_output = [[1, 6], [8, 10], [15, 18]]
        merged_meetings = self.meetings.merge_intervals(meetings)
        self.assertEqual(merged_meetings, expected_output)

        meetings = [[1, 2], [3, 4], [5, 6]]
        expected_output = [[1, 2], [3, 4], [5, 6]]
        merged_meetings = self.meetings.merge_intervals(meetings)
        self.assertEqual(merged_meetings, expected_output)

        meetings = [[1, 5], [2, 3], [4, 6]]
        expected_output = [[1, 6]]
        merged_meetings = self.meetings.merge_intervals(meetings)
        self.assertEqual(merged_meetings, expected_output)

        meetings = []
        expected_output = []
        merged_meetings = self.meetings.merge_intervals(meetings)
        self.assertEqual(merged_meetings, expected_output)

if __name__ == '__main__':
    unittest.main()
