class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freqMap = collections.defaultdict(int)
        for i in nums:
            freqMap[i] += 1
            if freqMap[i] == 2:
                return True
        return False
        