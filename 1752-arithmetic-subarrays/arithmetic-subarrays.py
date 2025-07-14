class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        result = []
        for i in range(m):
            new_sorted_array = sorted(nums[l[i]: r[i]+1])

            value_change = new_sorted_array[1] - new_sorted_array[0]
            # holder = True

            for num_index in range(len(new_sorted_array)-1):
                if new_sorted_array[num_index+1] - new_sorted_array[num_index] != value_change:
                    # holder =False
                    result.append(False)
                    break
            else:
                result.append(True)
            # result.append(holder)
        return result