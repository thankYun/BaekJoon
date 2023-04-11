import sys


def ChsQ(N):
    if N==0:
        return 0
    else:
        for x in range(N):
            Plate[x][x]+=1
        for y in range(N):
            Plate[y][x]+=1



N=int(sys.stdin.readline())

Plate=[[0 for _ in range(N)]for _ in range(N)]

for i in range(N):
    for y in range(i):
        for x in range(i):
            if Plate[y][x]==0:
                Plate[x][i]+=1
                Plate[i][y]+=1

        print(Plate)


#def
# 같은 x를 1을 더하고 다음 열로 넘어간다.
# 같은 y에 1을 더하겠다.
# x,y +(1,1) +(1,1) +(1,1)... n,n까지 반복하여 일치하는 x,y에 1을 더하겠다.
# if x,y 좌표의 내용이 ==0일때, 같은 x, y를 제거하고 위의 함수를 반복한다.
