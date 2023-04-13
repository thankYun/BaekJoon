import sys

N=int(sys.stdin.readline())
List=[0 for _ in range(N)]
for i in range(N):
    List[i]=sys.stdin.readline().rstrip()

set_List=set(List)
ListA=list(set_List)
ListA.sort()
ListA.sort(key=len)

for i in range(len(ListA)):
    print(ListA[i])