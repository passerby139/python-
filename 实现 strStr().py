class Solution:
    def strStr(self, haystack, needle):
        return haystack.find(needle)


str1 = input("haystack =")

str2 = input("needle =")

v = Solution()
print(v.strStr(str1,str2))
