# 문제
# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. 
#S에는 QR Code "alphanumeric" 문자만 들어있다.

# QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다. 각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. 
#S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

# 출력
# 각 테스트 케이스에 대해 P를 출력한다.

#입력에는 첫째 줄에 갯수가 주어지고 이후 주어진 갯수만큼
# R(정수), S(문자열) 가 들어갈 것이다 어떻게 하면 정수와 R을 모두 받을 수 있을까
#문자열로 받아서 R을 정수로 변형하겠다

T=int(input())
for i in range(T):
    R_1,S=map(input().split())
    R=int(R_1)



##TEST
    # S='rlaehddbs'
    # R=3

#S에 입력된 문자열을 각 텍스트로 어떻게 분리할 수 있을지를 생각해야 한다.
#검색 결과 String(start:end:step)함수를 찾았다. 사실 쓰고 보니 입학시험에서 공부했던 내용인 것 같은데 알콜성 청년치매는 그런 거 모른다.
#추가는 노션에 기입
# 방식이 특이한 것 같은데 추가로 공부가 필요하다. string.S 식일 줄 알았는데 string=S로 바로 S가 분리되어버린 것 같다.
    K=[]
# print(S*R)을 하면 123123123식으로 늘어진다.
    for i in range(len(S)):
    # print(S[i]*R)
    #를 하면 
    # 111 
    # 222
    # 333 식으로 분리되니 합쳐버리자.
        outPut=S[i]*R
        K.append(outPut)
# # string=K
# print(K)
#이제 리스트를 문자열로 합치자.
    join_K=''.join(K)
    print(join_K)




T=int(input())
for i in range(T):
    R_1,S=input().split()
    R=int(R_1)
    K=[]
    for i in range(len(S)):
        outPut=S[i]*R
        K.append(outPut)
    join_K=''.join(K)
    print(join_K)


# 하단은 모르는 사람이 푼 문제 방식을 참고하여, 내가 푼 방식에서 런타임 오류가 발생하여 역으로 문제가 되는 부분을 추적하기 위해 만들었다. map이 가장 큰 문제였던 듯.

# T=int(input())
# for i in range(T):
#     R_1,S=input().split()
#     R=int(R_1)
#     K=''
#     for j in range(len(S)):
#         outPut=R*S[j]
#         K+=outPut
#     print(K)
