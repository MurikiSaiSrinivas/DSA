class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n-1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        return longest
        # n = len(nums)
        # max_length = 0
        # for i in range(n):
        #     length = 0
        #     if nums[i]-1 in nums_set:
        #         continue
        #     length += 1
        #     newNum = nums[i] + 1
        #     while newNum in nums_set:
        #         length += 1
        #         newNum += 1
        #     max_length = max(max_length , length)
        # return max_length