# This function returns the room that has been booked the most times.
# It takes in an integer n, which represents the number of rooms, and a list of meetings.
# Each meeting is represented by a list of two integers, the start time and the end time.
# The function returns the room ID that has been booked the most times.

# def mostBooked(self, n, meetings):
#     """
#     :type n: int
#     :type meetings: List[List[int]]
#     :rtype: int
#     """
#     # Initialize a heap with all rooms and their end times set to 0
#     arr = []
#     for i in range(n):
#         heapq.heappush(arr, (0, i)) # (endTime, roomID)

#     # Initialize a counter to keep track of how many times each room has been booked
#     cnt = collections.Counter()

#     # Sort the meetings based on their start times
#     meetings.sort()

#     # Iterate through each meeting
#     for i in range(len(meetings)):
#         s, e = meetings[i]

#         # Free up any rooms that have finished being used
#         while arr[0][0] < s:
#             curTime, idx = heapq.heappop(arr)
#             heapq.heappush(arr, (s, idx))

#         # Book the current meeting in the room with the earliest end time
#         curTime, idx = heapq.heappop(arr)
#         heapq.heappush(arr, (max(curTime, s) + e - s, idx))
#         cnt[idx] += 1

#     # Find the room that has been booked the most times
#     maxV = 0
#     for i in range(n):
#         if cnt[i] > maxV:
#             res = i
#             maxV = cnt[i]
#     return res


"""
This code is a function that takes in an integer (n) and a list of meetings (meetings) as parameters, and returns the room index with the most booked meetings. It does this by using a heap to store the end times of each meeting in each room, and then iterating through the meetings list to find which room has been booked for the most amount of time.
"""


# :type n: int
# :type meetings: List[List[int]]
# :rtype: int


import heapq
from collections import Counter

def room_booking_count(n, meetings):
    # Initialize a heap with all rooms and their end times set to 0
    arr = []
    for i in range(n):
        heapq.heappush(arr, (0, i)) # (endTime, roomID)

    # Initialize a counter to keep track of how many times each room has been booked
    cnt = Counter()

    # Sort the meetings based on their start times
    meetings.sort()

    # Iterate through each meeting
    for i in range(len(meetings)):
        s, e = meetings[i]

        # Free up any rooms that have finished being used
        while arr[0][0] < s:
            curTime, idx = heapq.heappop(arr)
            heapq.heappush(arr, (s, idx))

        # Book the current meeting in the room with the earliest end time
        curTime, idx = heapq.heappop(arr)
        heapq.heappush(arr, (max(curTime, s) + e - s, idx))
        cnt[idx] += 1

    # Find the room that has been booked the most times
    maxV = 0
    for i in range(n):
        if cnt[i] > maxV:
            res = i
            maxV = cnt[i]
    return res


