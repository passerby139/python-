class Solution:
    def lengthOfLastWord(self, s: str):
                s = s.strip(' ')
                L = s.split(' ')[-1]
                return len(L)


num = "b   a    "
v = Solution()
print(v.lengthOfLastWord(num))
