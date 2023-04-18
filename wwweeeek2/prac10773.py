import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):    
    inp = int(sys.stdin.readline())
    
    if inp == 0:
        li.pop()
    else :
        li.append(inp)
print(sum(li))