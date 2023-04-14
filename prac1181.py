import sys

N=int(sys.stdin.readline())
List=[]
for i in range(N):
    Z=sys.stdin.readline
    if Z not in List:
        if len(List[i])>len(Z):
            List.insert(0,Z)
        elif len(List[i+1])>=len(Z)>len(List[i]):
            List.insert(i,Z)
        elif len(List[i+1])<len(Z):
            List.insert(i-1,Z)
        else:
            List.append(Z)

    

print(List)
# for i in range(len(List)):
#     print(List[i])