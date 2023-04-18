import sys

N=int(sys.stdin.readline())
Chk=[sys.stdin.readline() for _ in range(N)]
for i in range(10000):
    R=[Chk.count(i) for _ in range(N)]
for i in range(10000):
    if R[i] != 0:
        print (R[i]*str(i)) 