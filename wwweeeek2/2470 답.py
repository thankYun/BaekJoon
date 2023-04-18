import sys

N = int(sys.stdin.readline())
lia = list(map(int,sys.stdin.readline().split()))
lia.sort()

left = 0
right = N - 1

ans = abs(lia[left] + lia[right])
final = [lia[left],lia[right]]

while left<right:
    leftval = lia[left]
    rightval = lia[right]

    sum = leftval + leftval

    if abs(sum) < ans:   # 기존에 있던 절대값이 가장 작은 수보다 이번 합계의 절대값이 작다면(0에 가깝다면)
        ans=abs(sum)
        final=[leftval,rightval]
        if ans == 0:
            break        # ans가 0이면 더 이상 0에 가까울 수 없으므로 여기서 멈추고 출력한다.
        if sum < 0:
            left += 1
        else:
            right -= 1

print (final[0],final[1])