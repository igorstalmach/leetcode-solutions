class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        biggest = 0
        curr_biggest = 0
        start_index = 0
        num = 0
        temp = []

        while num < len(s):
            if s[num] not in temp:
                temp.append(s[num])
                num += 1
                curr_biggest += 1
                if curr_biggest > biggest:
                    biggest = curr_biggest
            else:
                temp = []
                curr_biggest = 0
                start_index += 1
                num = start_index
        
        return biggest