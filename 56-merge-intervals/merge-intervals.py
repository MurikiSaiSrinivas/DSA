class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        print(intervals)
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                values = sorted(intervals[i] + intervals[i+1])
                intervals = intervals[:i] + intervals[i+1:]
                intervals[i] = [values[0], values[-1]]
            else:
                i+=1
        return intervals