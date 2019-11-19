class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "[": "]", "{": "}"}
        strick = []
        for sur in s:
            if sur in dic.keys():
                strick.append(sur)
            elif sur in dic.values():
                if len(strick) == 0 or  dic.get(strick[-1]) != sur:
                    return False
                else:
                    strick.pop()
        if len(strick) == 0:
            return True
        else:
            return False




Str = input("请输入特殊字符串：")
son = Solution()
print(son.isValid(Str))