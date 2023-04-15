# A,B =map(int,input().split())
# K=list(range(max(2,A),B+1))
  
# for i in range(len(K)-1, -1, -1):
#     for j in range(2, int(K[i]**0.5)+1):
#         if K[i] % j == 0:
#             K.pop(i)
#             break
# for i in range(len(K)):
#     print(K[i])

# 함수를 사용했다. 나도 모르게 무슨 체까지 온 건 훌륭한데 문제는 시간 초과였다.
# sys를 임포트하는 등 방법을 사용했지만 계속 시간초과가 발생했고
# 결국 돌아돌아 GPT에 물어보니 pop 함수의 시간 복잡도가 O(n) -아무튼 굉장히 느림- 문제였다고 한다.
# GPT가 내 코드를 기반으로 다시 만든 코드다..

import sys
input=sys.stdin.readline()
A,B =map(int,input.split())
is_prime = [True] * (B-A+1)
# 가상의 함수를 만들어 트루의 갯수에 A이상 B 이하 정수의 갯수를 곱하는 것으로 정의했다.
# is_prime을 [true, true, true, true, true, true, true...] 식으로 놓은 것이다. 이걸 false로 변경하고 그 변수를 세려는 것으로 보인다.
# for 문을 통해 범위를 지정했다.
if A==1:
    A+=1
#GPT가 요걸 안 줬다. 내가 찾았다 ^^ 써글럼
for i in range(2, int(B**0.5)+1): 
    start = (A//i)*i
# start=A 를 정의하여 A가 i로 나누어떨어지지 않을 때 나머지가 발생하지 않도록 정의한 듯 하다.
    if start < A:
        start += i
# start에 i를 더한다는 것은 start를 i로 나누었을 때 1이 추가되도록 하겠다는 뜻으로 보인다.
# start<A가 뭘까? start/i의 나머지를 버리고 다시 i를 곱한 수가 start i가 아니라는 것은, start%i==0이 아닌 경우로 보인다.(나머지 없이 떨어지는 경우)
# 즉, 약수가 있는 경우 start에 1을 더한다.
    for j in range(start, B+1, i):  
        if j != i:
            is_prime[j-A] = False
#해당 부분은 i의 배수에 대해서 is_prime 리스트에서 해당 값을 False로 변경하는 부분입니다.

# 먼저, start 변수를 이용하여 소수 i의 배수 중에서 A 이상인 가장 작은 값을 계산합니다. 만약, start가 i와 같다면, start는 i의 배수가 아니므로 start 값을 2*i로 수정합니다. 
# 그리고, j가 i와 같은 경우에는 소수 i를 제외한 i의 배수이므로 is_prime[j-A] 값을 False로 변경합니다.

# 예를 들어, A=10, B=20, i=3인 경우, start=12가 됩니다. 이후, j의 값은 12, 15, 18, 21이 됩니다. j=12인 경우, j는 3의 배수이지만 j=i이므로, is_prime[j-A] 값은 변경되지 않습니다.
# j=15, 18인 경우, j는 3의 배수이면서 j!=i 이므로, is_prime[j-A] 값은 False로 변경됩니다.
# 라고 GPT께서 별빛으로 속삭이셨다.
for i in range(A, B+1):
    if is_prime[i-A]:
        print(i)