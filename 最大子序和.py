class Solution:
    def maxSubArray(self, nums):
        add = 0
        mas = nums[0]
        for i in nums:
            add += i
            if add > mas:
                mas = add
            if add < 0:
                add = 0
        return mas




num = [-2, 1]
v = Solution()
print(v.maxSubArray(num))