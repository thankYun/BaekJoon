import sys

N = int(sys.stdin.readline())
List = ['' for _ in range(N)]
via = [0 for _ in range(N)]
for i in range(N):
    via[i]=sys.stdin.readline().rstrip() # rstrip() 함수를 사용하여 개행 문자 제거)
via.sort()
print(via)
for i in range(N):
    if via[i] not in List:
        if len(List) == 0:
            List[len(List)]=via[i]
        else:
            for j in range(len(List)):
                if len(via[i]) < len(List[j]):
                    List[i]=via[i]                           #List.insert(j, via[i])
                    break
                elif j >= len(List[j]):
                    List[i-]
                    break
print(List)