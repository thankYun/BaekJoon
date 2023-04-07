# 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
floor=int(input())
if 0<floor<=100:
    for i in range (floor):
        print ("*"*(i+1))

#for문의 i가 0부터 시작했기 때문에 실제 출력을 했을 때
#한 층이 부족했다. 따라서 오답처리되었고 수정하여 정답처리되었다.