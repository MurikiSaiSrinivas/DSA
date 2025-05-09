from collections import defaultdict

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        prefix_sum = defaultdict(int)
        curr_sum = 0

        prefix_sum[0] = 1

        for num in nums:
            curr_sum += num
            result += prefix_sum[curr_sum - k]
            prefix_sum[curr_sum] += 1
        
        return result
