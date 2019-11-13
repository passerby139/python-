
class Solution():
    '''定义Solution类'''
    def arrangeCoins(self, n: int) -> int:
        '''搭建arrangeCoins方法,返回int类型值'''
        k=0
        if(n==1 ):
            return 1
        if(n==0):
            return 0
        else:
            for i in range(0,n+1):
                k=k+i
                if(n<k):
                    return(i-1)
                    break


n=int(input())
c=Solution()
print(c.arrangeCoins(n))









'''class Solution:
    def arrangeCoins(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n > c:
            c = c + 1
            n = n - c
        return c

v=Solution()

print(v.arrangeCoins(8))'''