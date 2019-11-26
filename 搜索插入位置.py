class Solution:
    def searchInsert(self, nums, target) -> int:
            for i in range(len(nums)):
                if target <= nums[0]:
                    return 0
                    break
                if target > nums[-1]:
                    return len(nums)
                    break
                if target == nums[-1]:
                    return len(nums)-1
                    break
                if nums[i] <= target and target <= nums[i+1]:
                        return i+1


num = [1, 3, 5, 6]
v=Solution()
print(v.searchInsert(num,0))