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

XY=list(zip(X,Y))
print(XY)

for i in range(N):
    for j in X:
        Plate[i][X[j]]+=1

print (Plate)
