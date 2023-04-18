# import sys

# N=int(sys.stdin.readline())
# N_list=[]
# for i in range(N):
#     N_list.append(list(map(int,sys.stdin.readline().split())))
# countBlue=[]


# def Cut4(start,xrange):
#     count=0
#     halfx=int(start+xrange/2)
#     if halfx != 0:
#         for i in range(start,halfx):
#             for j in range(start,halfx):
#                 count += N_list[i][j]
#         if count == (halfx)**2:
#             countBlue.append(1)
#         elif count != (halfx)**2 and count != 0:
#             Cut4(start,halfx)
        
#         count=0
#         for i in range(start+halfx,xrange):
#             for j in range(start+halfx):
#                 count += N_list[i][j]
#         if count == (halfx)**2:
#             countBlue.append(1)
#         elif count != 0:
#             Cut4(int(xrange/2),halfx)

#         count=0
#         for i in range(start,halfx):
#             for j in range(start+halfx,xrange):
#                 count += N_list[i][j]
#         if count == (halfx)**2:
#             countBlue.append(1)
            
#         elif count != (halfx)**2 and count != 0:
#             Cut4(halfx,int(xrange/2))
        
#         count=0
#         for i in range(start+halfx,xrange):
#             for j in range(start+halfx,xrange):
#                 count += N_list[i][j]
#         if count == (halfx)**2:
#             countBlue.append(1)
#         elif count != (halfx)**2 and count != 0:
#             Cut4(halfx,halfx)
# Cut4(0,N)
# print(sum(countBlue))


import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y]               #나눈 종이의 0,0 부분이 무엇인지 확인하고                                                                #그룹의 첫번째 놈이 1인지 0인지 확인
  for i in range(x, x+N) :
    for j in range(y, y+N) :
      if color != paper[i][j] :     #0,0과 다를 경우 종이를 4등분한다                                             #한 놈이라도 다르면 4개 함수 시도
        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 :
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))


니가 하고 싶던 함수 여기있다 동윤아~~~~~~~~~~~~~~~~~~~~~~~