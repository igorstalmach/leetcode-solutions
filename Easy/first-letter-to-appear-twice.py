# Runtime: 24 ms, faster than 99.35% of Python3 online submissions for First Letter to Appear Twice.
# Memory Usage: 13.8 MB, less than 96.59% of Python3 online submissions for First Letter to Appear Twice.

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict = {}

        for i in s:
            if i in dict:
                return i
            else:
                dict[i] = 1