class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        sum = 0

        for i in accounts:
            temp = 0
            
            for j in i:
                temp += j
            
            if temp > sum:
                sum = temp
        
        return sum