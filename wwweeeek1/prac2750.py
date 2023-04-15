# def Sort_Plus():

#         for j in range(len(A[i])):
#             if A[i][0]==Num[j]:
#                 A.insert(A[i].index())

# def Sort_Minus():
#     reversed(Sort_Plus())
    

N=int(input())
Num=list(str('0123456789'))
A=[]
B=[]
K=4
def Sooort(K):
    if K==0:
        print(0)
    else:
        Num=list(str('0123456789'))
        for i in range(N):
            B.append(list(str(A[i])))
            ind=Num.index(B[i][0])
            Num.insert(ind+1,A[i])
        print(Num)


for _ in range(N):
    A.append(int(input())%10**K)

Sooort(K)
print(A)
print(B)


# for i in range(N):
#     print(A[i])1