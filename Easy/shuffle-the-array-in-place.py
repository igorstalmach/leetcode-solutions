class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        for i in range(n, 0, -1): 
            nums.insert(i, nums.pop())
        
        return nums
