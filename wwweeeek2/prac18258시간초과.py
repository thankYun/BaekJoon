import sys

N=int(sys.stdin.readline())
li=[]

for i in range(N):
    inp=sys.stdin.readline().split()

    if inp[0]=='push':
        li.append(inp[1])
    if inp[0]=='pop':
        if len(li)== 0:
            print('-1')
        else:
            print(li[0])
            li.pop(0)
    if inp[0]=='size':
        print(len(li))
    if inp[0]=='empty':
        if len(li)== 0:
            print(1)
        else:
            print(0)
    if inp[0]=='front':
        if len(li)== 0:
            print('-1')
        else:
            print(li[0]) 
    if inp[0]=='back':
        if len(li)== 0:
            print('-1')
        else:
            print(li[-1])