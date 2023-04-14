import sys

N=int(sys.stdin.readline())
List=[0 for _ in range(N)]
for i in range(N):
<<<<<<< HEAD
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
=======
    List[i]=sys.stdin.readline().rstrip()
>>>>>>> 3cf09e7a73a1388a9d3827548a17480201a32d5e

set_List=set(List)
ListA=list(set_List)
ListA.sort()
ListA.sort(key=len)

<<<<<<< HEAD
print(List)
# for i in range(len(List)):
#     print(List[i])
=======
for i in range(len(ListA)):
    print(ListA[i])
>>>>>>> 3cf09e7a73a1388a9d3827548a17480201a32d5e
