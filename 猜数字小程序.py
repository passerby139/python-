import random
num=random.randint(1,100)
for i in range(1,11):
    word = int(input("请输入你猜测的数字："))
    if word == num:
        print("\n恭喜你猜对了！！正确答案是：",num)
        break
    elif(word>num):
        print("真垃圾，猜大了,第%d次机会失败"%i)
    elif (word < num):
        print("真垃圾，猜小了,第%d次机会失败"%i)
if i == 5:
    print("游戏挑战失败，正确数字为：",num)