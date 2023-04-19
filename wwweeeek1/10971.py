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

