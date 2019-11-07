nums=[2,7,11,15]


x=int(input("x:"))

def lengthOfLongestSubstring(test, x):
    for i in nums:
        for j in nums:
            if i+j == x:
                print('%d + %d = %d'%(i,j,x))

lengthOfLongestSubstring(nums, x)