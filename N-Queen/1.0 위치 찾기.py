#퀸이 놓일 수 있는 위치를 X,Y에 좌표로 기록함. X[i],Y[i]는 퀸이 놓일 수 있는 위치

import sys
N=int(sys.stdin.readline())
X=[]
Y=[]
# Plate=[[0 for _ in range(N)]for _ in range(N)]

Plate=[[0,0,1],[1,1,0],[1,1,0]]

for i in range(N):
    for j in range(N):
        if Plate[i][j]==0:
            Y.append(i)
            X.append(j)

print(Plate)
XY=list(zip(X,Y))
print(XY)