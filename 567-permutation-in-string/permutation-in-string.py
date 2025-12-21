class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        counter = Counter(s1)
        for i in range(len(s2) - n + 1):
            window_counter = Counter(s2[i: i+n])
            if counter == window_counter:
                return True
        return False

        # freq_s1 = [0]*26
        # for c in s1:
        #     freq[ord(c) - ord('a')] += 1
        
        # freq_tuple = tuple(freq_s1)

        # for in range()
