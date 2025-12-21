class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left<right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                remove_left = s[left+1:right+1]
                remove_right = s[left: right]
                return (remove_left == remove_left[::-1] or remove_right == remove_right[::-1])
        return True