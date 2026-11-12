class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 0:
            return 0
        x,y = 0,0 
        for money in nums:
            temp = x
            x = max(y+money, x)
            y = temp
        return x