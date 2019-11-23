class Solution:
    def removeElement(self, nums, val: int) -> int:
        i = 0
        l = len(nums)
        for count in range(l):
            if nums[i] != val:
                i = i + 1
            else:
                del nums[i]
        print(nums)
        return len(nums)


List = [0, 1, 2, 2, 3, 0, 4, 2]
num = 2
v = Solution()
print(v.removeElement(List,num))
