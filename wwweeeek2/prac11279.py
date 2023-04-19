import sys
import heapq
N = int(sys.stdin.readline())
li=[]

for i in range(N):
    inp=int(sys.stdin.readline().strip())

    if inp==0:
        try:
            print(-1*heapq.heappop(li)) # -1을 곱해 음수 중 절대값이 가장 큰 값을 불러오는 방식으로 최대 힙을 구현한다.
        except:
            print(0)
    else:
        heapq.heappush(li,-inp) # heappush는 기본적으로 최소 힙 기준으로 운용된다. 따라서 입력 시에 -를 붙여 최소값의 절대값>최댓값 이 되도록 -를 붙여 입력하고 ^ if inp==0에서