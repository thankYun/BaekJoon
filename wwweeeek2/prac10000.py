import sys

N=int(sys.stdin.readline())
li=[0 for _ in range(N)]
count=1
for i in range(N):
    li[i]=list(map(int,sys.stdin.readline().split()))

#원 양끝의 x 좌표를 어드레스로 입력
address=[0 for _ in range(N)]
for i in range(N):
    address[i]=([li[i][0]-li[i][1],li[i][0]+li[i][1]])

via=[]
for i in range(N):
    if i==0:
        via.extend(address)
    for j in range(N):
        if via[i][0]==address[j][0]:
            continue
        elif via[i][1]==address[j][1]:
            continue
        elif via[i][1]==address[j][0]:
            via.append([via[i][0],address[j][1]])
for i in range(len(via)):
    if via[i] in address:
        count+=1
print(count)