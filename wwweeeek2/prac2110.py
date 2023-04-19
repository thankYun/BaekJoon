import sys
N,M = map(int,sys.stdin.readline().split())
Nlist = []
for i in range(N):
    Nlist.append(int(sys.stdin.readline()))
Nlist.sort()

def bi_search():
    start=Nlist[0]
    end=Nlist[N-1]-Nlist[0]

    while start+1<end:
        mid = (start+end)//2
        count=1
        now=Nlist[1]
        for i in range(M-2):
            if mid >= (start-end)*i//(M-1):
                start=mid
                break
            else:
                end=mid
    return 
print(bi_search())