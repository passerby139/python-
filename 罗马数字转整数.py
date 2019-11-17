class Solution:
    def romanToInt(self, s: str) -> int:
        add=0
        dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for k in range(len(s)):
            if len(s) <= 1:
                add = dic[s[0]]
                break
            for i, j in dic.items():
                if s[k] == i:
                    add =  add+j
                    if (dic[s[k]] > dic[s[k-1]]) and (k != 0):
                        if (s[k-1] == 'I') or (s[k-1] == 'X') or (s[k-1] == 'C'):
                            add = add - 2 * dic[s[k-1]]
        print(add)

NUM = input("请输入一个罗马数字：")
c = Solution()
c.romanToInt(NUM)