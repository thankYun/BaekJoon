# 문제
# "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

# 출력
# 각 테스트 케이스마다 점수를 출력한다.
# def SumNum(n):
#     if n == 0:
#         return 0
#     else:
#         return n+SumNum(n-1)


# # OX_Time=int(input())

# SpList=List_OX.split('X')
# ForSum=[]
# # for i in range(OX_Time):
# # #     List_OX.append(input().split('X'))
# for j in range (len(SpList)):
#     A=SumNum(SpList[j].count('O'))
#     ForSum.append(A)
# print(sum(ForSum))

#입력값에서 X를 기준으로 항목을 분리한다.
#항목의 O의 갯수를 세어 갯수+(갯수-1)...을 한다 > sumnum
#개수를 list로 저장하고 sum함수를 통해 더한다.
#이를 출력한다.

def sumNum(n):
    if n == 0:
        return 0
    else:
        return n + sumNum(n-1)
n+=1
OXT = int(input())

for i in range(OXT):
    A=input().split('X')
    forSum=[]
    for j in range(len(A)):
        B = sumNum(A[j].count('O'))
        forSum.append(B)
    print(sum(forSum))