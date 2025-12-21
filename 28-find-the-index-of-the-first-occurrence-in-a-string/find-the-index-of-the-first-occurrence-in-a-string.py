class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        # if n == m and haystack == needle:
        #     return 0
        for i in range(n + 1 - m):
            if haystack[i: i+m] == needle:
                return i
        return -1