a=int(input("plase:"))
b=[]

for i in range(1,a+1):
    c=int(input())
    b.append(c)

b.sort()
for i in range(0,a):
    print(b[i],end=' ')
