import sys

N= int(sys.stdin.readline())
Nlist=list(map(int,sys.stdin.readline().split()))
M= int(sys.stdin.readline())
Mlist=list(map(int,sys.stdin.readline().split()))
Nlist.sort()
def binary_search(target, data):

    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None


target = Mlist
for i in range(M):
    binary_search(Mlist[i],Nlist)
    if binary_search(Mlist[i],Nlist) is not None:
        print(1)
    else:
        print(0)