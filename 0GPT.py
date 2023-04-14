def SumNum(n):
    if n == 0:
        return 0
    else:
        return n + SumNum(n-1)

OXT = int(input())
OX = []
ForSum = []
for i in range(OXT):
    OX.append(input().split('X'))
    Sum = 0
    
    for j in range(len(OX[i])):
        A = OX[i][j].count('O')
        Sum += SumNum(A)
    ForSum.append(Sum)
    print(ForSum[i])