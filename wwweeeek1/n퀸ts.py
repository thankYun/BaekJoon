import sys

N=int(sys.stdin.readline())

Plate=[[0 for _ in range(N)]for _ in range(N)]
for i in range (N):
    Plate[1][i]+=1

print (Plate)