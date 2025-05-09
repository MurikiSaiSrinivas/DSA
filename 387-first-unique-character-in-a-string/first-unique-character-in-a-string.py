from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq_map = defaultdict(int)
        for char in s:
            freq_map[char] += 1
        
        for index, char in enumerate(s):
            if freq_map[char] == 1:
                return index
        return -1
        