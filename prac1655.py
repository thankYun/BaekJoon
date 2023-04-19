import sys
from collections import deque
N=int(sys.stdin.readline())
li=deque([])
stage=deque([])
for i in range(N):
    a=int(sys.stdin.readline())
    if len(li) == 0:
        li.append(a)
    elif li[-1]<a:
        li.append(a)
    else:
        while a > li[0]:
            stage.append(li[0])
            li.popleft()
            if len(li) == len(stage)+1:
                    print(li[0])
            elif len(li) == len(stage) :
                    print(stage[-1])
        while len(li) != 0:
            li.append(stage[0])
            stage.popleft()
        li.append(a)
        li.append(li[0])
        li.popleft()
