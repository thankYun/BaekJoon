import sys
N=int(sys.stdin.readline())
A=[]
B=[]
sett=[]
List=[map(int,sys.stdin.readline().split())]
List.sort()

if N%2==1:
    if List[N//2]-List[N//2-1]>=List[N//2-1]-List[N//2-2]:
        for i in range(N//2+1):
            A.append(List[i])
        for i in range(N//2+1,N):
            B.append(List[i])
            B.reverse()
print(A)
print(B)



        # sett.append(B[0])
        # for i in range(1,N//4):
        #     sett.append(A[i*2-1])
        #     sett.append(A[i*2])
        #     sett.append(B[i*2-1])
        #     sett.append(B[i*2])


#     else:
#         for i in range(N//2):
#             A.append(List[i])
#         for i in range(N//2,N):
#             B.append(List[i])
# else: