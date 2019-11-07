import random
randomnumber=[random.randint(10,100)for i in range(10)]
print("生成的随机数为：",randomnumber)
newlist=[int(x*0.5)for x in randomnumber]
print("0.5倍原数：",newlist)
nextlist=[x for x in newlist if x>30]
print("高于30的:",nextlist)
