def Hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        Hanoi (N-1,a, c, b) ## 홀 짝인 경우마다 c b를 바꾸어주는 행위 (N-1)인 경우 무조건 짝수>홀수 // 홀수 >> 짝수가 되므로 무조건 사용된다.
        Hanoi (1, a, b, c)  ## 직전의 하노이 순서대로 옮김 A에서 옮기는 가장 큰 원판을 옮기는 행위
        Hanoi (N-1, b, a, c) ## 위 else에서 -2칸씩 밀었다. C>A B>C A>B로. 수열을 통해 이 규칙을 확인하였다.

N=int(input())
count=0
if N <= 20:
    for i in range(N):
        count += 2**i
    print (count)
    Hanoi(N, 1, 2, 3)