import sys

N=int(sys.stdin.readline())
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
