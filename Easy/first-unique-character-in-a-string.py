class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict = {}

        for i in s:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        
        for key, val in dict.items():
            if val == 1:
                return s.index(key)
        
        return -1