import sys

N=int(sys.stdin.readline())
<<<<<<< HEAD
Plate=[]
for i in range(N):
    iprurk=sys.stdin.readline().split()
p   if iprurk=='push': 
        Plate.append(iprurk[1])
    if iprurk=='pop' :
        if Plate==[]:
            print(-1)
        else:
           Plate.pop()
    if iprurk=='size' :
        print(len(Plate))
    if iprurk=='empty':
        if Plate==[]:
            print(1)
        else:
            print(0)
    if iprurk=='top':
        print(Plate[-1])
=======
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
>>>>>>> 425d5475162f0a4f1258a355afef2fed9fd25e18
