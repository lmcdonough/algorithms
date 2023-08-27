from typing import List, int

class Meetings:
    """
    A class that contains a method to merge overlapping meetings.

    Attributes:
    -----------
    None

    Methods:
    --------
    merge_intervals(meetings: List[List[int]]) -> List[List[int]]:
        Given a list of meetings, merge all overlapping meetings and return a list of non-overlapping meetings.

    Example:
    --------
    meetings = Meetings()
    meetings.merge_intervals([[1,3],[2,6],[8,10],[15,18]])
    # Output: [[1,6],[8,10],[15,18]]
    """

    def merge_intervals(self, meetings: List[List[int]]) -> List[List[int]]:
        """
        Given a list of meetings, merge all overlapping meetings and return a list of non-overlapping meetings.

        Parameters:
        -----------
        meetings : List[List[int]]
            A list of meetings where each meeting is represented by a list of two integers [start_time, end_time].

        Returns:
        --------
        List[List[int]]
            A list of non-overlapping meetings where each meeting is represented by a list of two integers [start_time, end_time].

        Example:
        --------
        meetings = Meetings()
        meetings.merge_intervals([[1,3],[2,6],[8,10],[15,18]])
        # Output: [[1,6],[8,10],[15,18]]
        """
        # validate input
        if meetings is None:
            return []
        if len(meetings) == 1:
            return meetings

        # sort the meetings by start time
        meetings.sort(key=lambda x: x[0])
        # or use the operator.itemgetter which is faster than using lambda for sorting
        # meetings.sort(key=operator.itemgetter(0))

        # create containers/cursors/temp vals
        large_meetings = []
        start_time = meetings[0][0]
        end_time = meetings[0][1]

        # iterate
        for meeting in meetings:
            # math
            st = meeting[0]
            et = meeting[1]

            if st >= end_time:
                large_meetings.append([start_time, end_time])
                start_time = st
            end_time = max(end_time, et)
                
        # append the last meeting
        large_meetings.append([start_time, end_time])

        # return list of consolidated meetings
        return large_meetings