
#zip함수
#a=[1,2,3]
#b=[4,5,6]
#list(zip(a,b))
#[(1,2),(3,4),(5,6)]
#tuple(zip(a,b))
#((1,2),(3,4),(5,6))

import sys
N=int(sys.stdin.readline())
X=[]
Y=[]
# Plate=[[0 for _ in range(N)]for _ in range(N)]

Plate=[[1,1,1],[1,1,0],[1,1,0]]

# for 변수 in range(N):
#     Plate[y][변수]+=1      y번쨰 행에 전체 1 추가

# for 변수 in range(N):      x번째 열에 전체 1 추가
#     Plate[변수][x]+=1 

#퀸이 놓일 수 있는 위치를 X,Y에 좌표로 기록함. X[i],Y[i]는 퀸이 놓일 수 있는 위치
for i in range(N):
    for j in range(N):
        if Plate[i][j]==0:
            Y.append(i)
            X.append(j)

#퀸이 X[i],Y[j]에 놓였을 때 x좌표==X[i], y좌표==Y[j]인 곳 모두에 +=1 
list(map(+1),Plate[1])


print(X)
print(Y)
# for i in range(N):
#     Plate[y][i]+=1
#     Plate[i][x]+=1
print (Plate)