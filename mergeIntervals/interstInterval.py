"""Given a list of non-overlapping intervals sorted by their start time,
 insert a given interval at the correct position and merge all necessary
  intervals to produce a list that has only mutually exclusive intervals. 
  
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
  """


    def insert(self, intervals, new_interval):
        merged = []
        # TODO: Write your code here
        i=0

        while i < len(intervals) and intervals[i].end < new_interval.start:
            merge.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i].start <= new_interval.end:
            new_interval.start = min(intervals[i].start, new_interval.start)
            new_interval.end = max(interval[i].end, new_interval.end)
            i+= 1
        merge.append(new_interval)

        while i < len(intervals):
            merge.append(intervals[i])
            i+=1
        return merged
