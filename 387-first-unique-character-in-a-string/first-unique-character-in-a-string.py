from collections import defaultdict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        freq_map = defaultdict(int)
        for index, char in enumerate(s):
            freq_map[char] += 1
            while result < len(s) and freq_map[s[result]] > 1:
                result += 1
        return result if result < len(s) else -1