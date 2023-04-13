import sys

nan = []
for _ in range(9):
    nan.append(int(sys.stdin.readline().rstrip()))

N = len(nan)
sumnan = sum(nan)

for i in range(N):
    for j in range(i+1, N):
        if sumnan - nan[i] - nan[j] == 100:
            nan2 = list(nan)
            nan2.remove(nan[i])
            nan2.remove(nan[j])
nan2.sort()
for k in range(7):
    print(nan2[k])
