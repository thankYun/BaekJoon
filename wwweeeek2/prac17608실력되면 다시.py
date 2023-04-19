import sys

N=int(sys.stdin.readline())
lis=[]
setlis=[]
count=1

for _ in range(N):
    lis.append(int(sys.stdin.readline()))
lis.reverse()
for i in lis:
    if i not in setlis:
        setlis.append(i)

# for _ in range(N):
#     setlis.append(int(sys.stdin.readline()))
# setlis.reverse()

for i in range(len(setlis)):
    for j in range (i+1,len(setlis)-1):
        if setlis[j]<=setlis[i]:
            setlis.pop(j)
    for j in range (i+1,len(setlis)-1):
        if setlis[j]>setlis[i]:
            count+=1

print(count)
