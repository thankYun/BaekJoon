import sys

N= int(sys.stdin.readline())
lia=sys.stdin.readline().split()
lia.sort()

def bi_search(target,data):
    start=0
    end=len(data)-1

    while start< end:
        mid = (start+end) // 2
        if data[mid] == target:
            return mid
        elif data[mid]<target:
            start = mid + 1
        else:
            end = mid - 1

    return None

for i in lia:
    bi_search(i,lia)