import sys
N=int(sys.stdin.readline())
for i in range(N):
    A=list(map(int,sys.stdin.readline().split()))
B=[0 for _ in range(10001)]
print(A)
for i in A:
    B[i]+=1
for i in range(len(B)):
    if B[i]!=0:
        for _ in range(B[i]):
            print(i)
