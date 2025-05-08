class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_arr = []
        suffix_arr = [1] * len(nums)
        result = [1] * len(nums)

        prefix = 1
        for num in nums:
            prefix_arr.append(prefix)
            prefix *= num
        
        suffix = 1
        for index in range(len(nums)-1, -1, -1):
            suffix_arr[index] = suffix
            suffix *= nums[index]
        
        for i in range(len(nums)):
            result[i] = prefix_arr[i] * suffix_arr[i]
        return result
