import sys

N=int(sys.stdin.readline())
lis=[]

count=0

for _ in range(N):
    lis.append(int(sys.stdin.readline()))
max=0
lis.reverse()
for i in lis:
    if i>max:
        count+=1
        max=i

print(count)
