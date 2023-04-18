import sys
from collections import deque

N=int(sys.stdin.readline())
li=deque([])

for i in range(N):
    inp=sys.stdin.readline().split()
    if inp[0]=='push':
        li.append(inp[1])
    if inp[0]=='pop':
        if len(li)== 0:
            print('-1')
        else:
            print(li[0])
            li.popleft()
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