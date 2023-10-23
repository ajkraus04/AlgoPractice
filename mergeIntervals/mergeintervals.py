"""Given a list of intervals, merge all the overlapping intervals 
to produce a list that has only mutually exclusive intervals.

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
"""

def merge_intervals(intervals):
    if len(intervals) < 2:
        return intervals
    merged_intervals = []
    organized_intervals = sorted(intervals, key=lambda x: x.start)
    start = organized_intervals[0].start
    end = organized_intervals[0].end
    for i in range(1,len(intervals)):
        if intervals[i].start <= end:
            end = max(end, intervals[i].end)
        else:
            merged_intervals.append([start,end])
            start = intervals[i].start
            end = intervals[i].end
    merged_intervals.append([start,end])
    return merged_intervals
        
    

merge_intervals([[6,7], [2,4], [5,9]])
