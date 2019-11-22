class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0  # 当前元素下标i 初始化
        l = len(nums)  # 取长度
        for count in range(l-1):  # count用于累计相邻两个数比较的次数
            print("新一轮开始时count值为："+str(count))
            if nums[i] != nums[i + 1]:  # 相邻两个数不相同
                i += 1
                count += 1
            else:  # 相邻两个数相同
                del nums[i + 1]  # 删除后一个数
                count += 1
            print("这一轮结束时count值为："+str(count)+"\n")
        return len(nums)
nums = [0,1,1,2,2,2,3,4,4,5]
v=Solution()
print(v.removeDuplicates(nums))

