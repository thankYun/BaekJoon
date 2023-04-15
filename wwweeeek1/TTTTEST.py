# inpNew1=[1,3]
# inpNew2=[1,2]

# def Hanoi(N):
#     if N == 0:
#         pass
#     elif N % 2 != 0:
#         return HanoiOdd(N)
#     else:
#         return HanoiEven(N)
    
# def HanoiOdd(N):
#     if N==1:
#         return inpNew1
#     else:
#         return HanoiOdd(N-2)

# def HanoiEven(N):
#     if N == 2:
#         return inpNew1
#     else:
#         if N%2 !=0:
#             return HanoiEven(N-2)
        
# # N==0일때
# #     pass
# # N==홀수
# #     HanoiOdd 사용
# # 나머지
# #     HanoiEven 사용

inpNew1=[1,3]
inpNew2=[1,2]

def Hanoi(N):
    if N == 0:
        pass
    elif N== 1 or 2:
        print (inpNew1)
        return(inpNew1)
    elif N % 2 != 0:
        print (inpNew1)
        return(inpNew1)
    else:
        print (inpNew1)
        return(inpNew1)
