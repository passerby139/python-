name=['蒋文隆','翟羽佳','蒋子赟']
sign=('天秤座','白羊座','双鱼座')
val=dict(zip(name,sign))             #现将双列表(可以是双元祖或者一个元祖一个列表)合并转成元祖，再转成字典输出
print(val)
print(val['蒋文隆'])


for i in val.items():                #遍历数组进行输出
    print(i)


val['蒋文隆']='大帅哥'
print('\n'+val['蒋文隆'])