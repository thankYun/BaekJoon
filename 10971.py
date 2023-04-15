import sys

N=int(sys.stdin.readline())
visited=[False]*N

list=[list(map(int,sys.stdin.readline().split()))]
Minfind=[]

def dfs(li):
    if len(li)==N:
        A=0
        for i in range(N):
            A+=li[i]
        Minfind.append(A)
    for i in range(N):
            if not visited[i]:
                visited[i]=True
                li.append(list[i])
                dfs(li)
                visited[i]=False
                li.pop()

dfs([])
print (min(Minfind))


import sys


def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N
for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)
profile
유현민