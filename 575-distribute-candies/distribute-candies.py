class Solution(object):
    def distributeCandies(self, candyType):
        """
        :type candyType: List[int]
        :rtype: int
        """
        unique_types = set(candyType)
        return min(len(unique_types), len(candyType) // 2)