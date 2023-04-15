def decombine():
    A=B
def combine():                                                              #1 큰 수를 가진 함수로 이동
    for i in range (count,0,-1):
        if i == 0:
            print('1 2')
        elif i == 1:
            print('1 3')
        else:
            if A[0]+1==B[0]:
                B.insert(0,A[0])
                print('1 2')
                A.pop(0)
            elif A[0]+1==C[0]:
                C.insert(0,A[0])
                print('1 3')
                A.pop(0)
            elif B[0]+1==A[0]:
                A.insert(0,B[0])
                print('2 1')
                B.pop(1)
            elif B[0]+1==C[0]:
                C.insert(0,B[0])
                print('2 3') 
                B.pop(0)
            elif C[0]+1==A[0]:
                A.insert(0,C[0])
                print('3 1')
                C.pop(0)
            elif C[0]+1==B[0]:
                B.insert(0,C[0])
                print('3 2')
                C.pop(0)
N=int(input())
count=0
for i in range(N):
    count += 2**i
print (count)

A=list(range(3,N+1))
B=[2]
C=[1]

print (A)
print (B)
print (C)


# 인접하는 자연수가 없을 때
if (len(B)+len(C))%2 != 0:
    if len(B==0):
        B.append(A[0])
        A.pop(0)
    elif len(C==0):
        C.append(A[0])
        A.pop(0)
    
