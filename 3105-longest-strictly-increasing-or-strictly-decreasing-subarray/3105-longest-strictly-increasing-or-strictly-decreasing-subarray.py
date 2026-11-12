class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = True
        res = 1
        ans = []
        if len(nums) < 2:
            return 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]: #inc
                if inc:
                    res += 1
                else:
                    inc = True
                    ans.append(res)
                    res = 2
            elif nums[i] < nums[i-1]:
                if not inc:
                    res += 1
                else:
                    inc = False
                    ans.append(res)
                    res = 2
            else:
                ans.append(res)
                res = 1
        return max(1 if not ans else max(ans), res)

