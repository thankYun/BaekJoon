import sys

N=int(sys.stdin.readline())
li=[0 for _ in range(N)]
count=1 #N 일반적으로 원의 갯수만큼 늘어나 1+N이 되어야 하지만, 
        #마지막에 via에 address가 포함되어 있으므로 N을 더하지 않았다.
for i in range(N):
    in0, in1=map(int,sys.stdin.readline().split())
    li[i]=[in0-in1,in0+in1]

via=[]
for i in range(N):
    if i==0:
        via.extend(li)
    for j in range(N):
        if via[i][0]==li[j][0]:
            continue
        elif via[i][1]==li[j][1]:
            continue
        elif via[i][1]==li[j][0]:
            via.append([via[i][0],li[j][1]])
for i in range(len(via)):
    if via[i] in li:
        count+=1
print(count)