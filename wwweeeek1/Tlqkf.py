import sys
N = int(sys.stdin.readline())
B = [0 for _ in range(10001)]
for i in range(N):
    A = int(sys.stdin.readline())
    B[A] += 1
 
for i in range(10001):
    if B[A]!=0:
        for j in range(B[i]):
            print(i)