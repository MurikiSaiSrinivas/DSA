class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        leftBorder = [0] * len(height)
        rightBorder = [0] *len(height)
        nextBorder = 0
        for i in range(len(height)):
            leftBorder[i] = nextBorder
            nextBorder = max(nextBorder,height[i])
        nextBorder = 0
        for i in range(len(height)-1, -1, -1):
            rightBorder[i] = nextBorder
            nextBorder = max(nextBorder, height[i])
        waterCount = 0 
        for i in range(len(height)):
            minBorder = min(leftBorder[i], rightBorder[i])
            if  minBorder - height[i] > 0:
                waterCount += (minBorder-height[i])
        return waterCount