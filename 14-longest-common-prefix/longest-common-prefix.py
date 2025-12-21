class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_common_prefix = ""
        for idx, char in enumerate(strs[0]):
            for i in range(len(strs)):
                if idx >= len(strs[i]) or strs[i][idx] != char:
                    return longest_common_prefix
            longest_common_prefix += char
        return longest_common_prefix 

        