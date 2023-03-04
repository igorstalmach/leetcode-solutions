class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        new_list = []

        for i in range(n):
            new_list.append(nums[i])
            new_list.append(nums[n+i])
        
        return new_list
