import sys

N = int(sys.stdin.readline())
List = []
via = []
for i in range(N):
    via+=([input()])
via.sort()
print(via)
for i in range(N):
    if via[i] not in List:
        if len(List) == 0:
            List+=[via[i]]
        else:
            for j in range(len(List)):
                if len(via[i]) < len(List[j]):
                    List.insert(j, via[i])
                    break
                elif j == len(List) - 1:
                    List.append(via[i])

print(List)