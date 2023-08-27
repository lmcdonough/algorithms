from merge_intervals import Meetings

def test_merge_intervals():
    meetings1 = [[1, 4], [3, 5], [2, 6]]
    expected1 = [[1, 6]]
    assert Meetings().merge_intervals(meetings1) == expected1

    meetings2 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected2 = [[1, 6], [8, 10], [15, 18]]
    assert Meetings().merge_intervals(meetings2) == expected2

    meetings3 = [[1, 4], [4, 5]]
    expected3 = [[1, 5]]
    assert Meetings().merge_intervals(meetings3) == expected3

    meetings4 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    expected4 = [[1, 5]]
    assert Meetings().merge_intervals(meetings4) == expected4

    meetings5 = [[1, 2], [3, 4], [5, 6]]
    expected5 = [[1, 2], [3, 4], [5, 6]]
    assert Meetings().merge_intervals(meetings5) == expected5

    meetings6 = [[1, 2]]
    expected6 = [[1, 2]]
    assert Meetings().merge_intervals(meetings6) == expected6

    meetings7 = []
    expected7 = []
    assert Meetings().merge_intervals(meetings7) == expected7