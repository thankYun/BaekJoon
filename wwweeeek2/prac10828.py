import sys

N=int(sys.stdin.readline())
li=[]
for i in range(N):
    listinput=sys.stdin.readline().split()

    if listinput[0]=='push':
        li.append(listinput[1])

    elif listinput[0]=='pop':
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])
            li.pop()
            

    elif listinput[0]=='size':
        print(len(li))

    elif listinput[0]=='empty':
        if len(li)==0:
            print(1)
        else:
            print(0)

    elif listinput[0]=='top':
        if len(li)==0:
            print(-1)
        else:
            print(li[-1])