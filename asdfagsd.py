import sys

N = int(sys.stdin.readline())
List = []
lengths = []
for i in range(N):
    Z = sys.stdin.readline()
    if len(Z) not in lengths:
        lengths.append(len(Z))
        if len(List) == 0:
            List.append(Z)
        else:
            for j in range(len(List)):
                if len(Z) < len(List[j]):
                    List.insert(j, Z)
                    break
                elif j == len(List) - 1:
                    List.append(Z)

print(List)
3