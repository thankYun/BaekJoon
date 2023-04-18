import sys
N, M = map(int,sys.stdin.readline().split())
Nlist = list(map(int,sys.stdin.readline().split()))
Nlist.sort()
def biSearch():
    start = 0
    end = Nlist[N - 1]
    while start+1 < end:                                    #start+1<end /// start<end-1 /// start<end ////start<=end 등등 다양한 경우가 있다.
        mid = (start+end) // 2
        cut = 0
        for i in Nlist:
            if i > mid:
                cut += i - mid
            if cut > M :
                break
        if cut >= M:
            start = mid
        else:
            end = mid
    return start

print(biSearch())