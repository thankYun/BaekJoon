import sys
N=int(sys.stdin.readline())
c=0
li=[]
for _ in range(N):
    li.extend(str(sys.stdin.readline().split()))
    c=0
    for i in range(len(li)):
        if li[i]=='(':
            c += 1
        elif li[i]==')':
            c += -1
            if c<0:
                print('NO')
                li=[]
                break
    if c==0:
        print('YES')
    elif c>0:
        print('NO')
    li=[]