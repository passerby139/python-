class Solution:
    def reverse(self, x: int) -> int:
        list=[]
        ADD=0
        use=0
        if x<0:
            use=x
            x=x*-1
        while 1:
            y = x % 10
            list.append(y)
            x = x // 10
            if x == 0:
                break
        for i in range(len(list)):
            ADD = ADD * 10 + list[i]
        if (-2147483648 <= ADD and ADD <= 2147483647):
            if use<0 :
                return -ADD
            else:
                return ADD
        else:
            return 0

y=int(input("x:"))

test=Solution()
print(test.reverse(y))

