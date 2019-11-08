f1=1
f2=1
add=0
n=int(input())
if n+1>3:
    for i in range(3,n+1):
        add=f1+f2
        f1=f2
        f2=add
if n==1:
    add=f1
if n==2:
    add=f1+f2

add=add%10007
print(add)