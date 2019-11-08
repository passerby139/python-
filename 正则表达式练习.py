import re                           #调用正则库

a='zxcvb123'
b=re.findall('\d+',a)               #搜寻a字符串中所有数字合为一个列表
b1=re.findall('\d',a)               #搜寻a字符串中所有数字分为一个列表
print('b=',b)
print('b1=',b1)


c=re.findall('v*',a)                #搜寻a字符串中v字符，没有的输出空，合为一个列表
print('c=',c)



code='djhuxxIxxdfnjwxxLovexxdjf13254dfxxyouxxefehfer'
d=re.findall('xx.*xx',code)          #搜寻code字符串中"xx-xx"形式中间的所有字符（贪心算法）合为一个列表
e=re.findall('xx.*?xx',code)         #搜寻code字符串中"xx-xx"形式中间的字符（非贪心算法）合为一个列表
print('d=',d)
print('e=',e)

f=re.findall('xx(.*?)xx',code)       #搜寻code字符串中"xx-xx"形式中间的字符，并去除xx存入合为一个列表
print('f=',f)



newline='''dsfbkjfxxhello
xxdsfsxxworldxxerjfr'''
g=re.findall('xx(.*?)xx',newline)
print('g=',g)
h=re.findall('xx(.*?)xx',newline,re.S)          #re.S代表寻找时包含\n换行
print('h=',h)