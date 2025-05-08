class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        checkedNums = dict()
        for index in range(len(nums)):
            hasCompliment  = checkedNums.get(target - nums[index], -1)
            if hasCompliment != -1:
                return [hasCompliment, index]
            checkedNums[nums[index]]= index
        return -1

        