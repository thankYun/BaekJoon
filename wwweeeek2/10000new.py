import sys
sys.setrecursionlimit(300000)

N=int(sys.stdin.readline())
li=[0 for _ in range(N)]
count=1 #N 일반적으로 원의 갯수만큼 늘어나 1+N이 되어야 하지만, 
        #마지막에 via에 address가 포함되어 있으므로 N을 더하지 않았다.

#x의 양쪽 끝을 좌표로 넣었다.
for i in range(N):
    in0, in1=map(int,sys.stdin.readline().split())
    li[i]=[in0-in1,in0+in1]

def convergence(M,via):
    if M-N==0:
        via.extend(li)
    for i in range(M):
        if via[N-M][0]==li[i][0]:
            continue
        elif via[N-M][1]==li[i][1]:
            continue
        elif via[N-M][1]==li[i][0]:
            via.append([via[N-M][0],li[i][1]])
    return convergence(M-1,via)    
convergence(N,[])
for i in range(len(via)):
    if via[i] in li:
        count+=1
        print(count)