import sys

N=int(sys.stdin.readline())
List=[]
for i in range(N):
    Z=input()
    if Z in List:
        pass
    else:
        for j in range (len(List)):
            if len(List[j])>len(Z)>len(List[j-1]):
                List.insert(j,Z)

    


# for i in range(len(List)):
#     print(List[i])