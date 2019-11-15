class Flower:
    def FindFlower(self,x:int):
        list=[]
        Add=0
        Y=x
        while 1:
            y=x%10
            list.append(y)
            x=x//10
            if(x==0):
                break
        for i in range(len(list)):
            Add=Add+list[i]*list[i]*list[i]
        if (Add==Y):
            return Y

c=Flower()
h=int(input('请输入一个数：'))

if(c.FindFlower(h)==None):
    print(str(h)+"不是水仙花数")
else:
    print(str(h)+"是水仙花数")