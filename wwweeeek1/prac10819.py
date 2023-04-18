import sys

N=int(sys.stdin.readline())
visited=[False]*N
list=list(map(int,sys.stdin.readline().split()))
Maxfind=[]
def gap(li):
    if len(li)==N:
        A=0
        for i in range(N-1):
            A+=abs(li[i]-li[i+1])
        Maxfind.append(A)
        return
    for i in range(N):
        if not visited[i]:
            visited[i]=True
            li.append(list[i])
            gap(li)
            visited[i]=False
            li.pop()

gap([])
print(max(Maxfind))