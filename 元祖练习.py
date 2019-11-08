vel=tuple(range(10,200,2))     #利用tuple函数实现元祖创建
print(vel)
print(vel[0],vel[-1])           #利用索引寻找元祖

test=(1,2,3,4)
test=test+(4,5)
print("组合后：",test)

import random
suiji=(random.randint(1,101)for i in range(10))
suiji=tuple(suiji)
print(suiji)