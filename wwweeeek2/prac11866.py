import sys
sys.setrecursionlimit(5000000)
from collections import deque
N,K=map(int,sys.stdin.readline().split())
liA=deque([])
liB=[]
for i in range(N):
    liA.append(i+1)

def yo(n):
    if len(liA)==0:
        return
    elif (n)%K==0:
        liB.append(liA[0])
        liA.popleft()
    else:
        liA.append(liA[0])
        liA.popleft()
    return yo(n+1)
yo(1)
for i in range(len(liB)+2):
    if i == 0:
        print('<', end="")
    elif i == len(liB)+1:
        print('>')
    elif i == len(liB):
        print(liB[i-1], end="")
    else:
        print(liB[i-1], end=", ")