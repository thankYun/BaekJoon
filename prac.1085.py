#한수는 지금 (x, y)에 있다. 
#직사각형은 각 변이 좌표축에 평행하고, 
#왼쪽 아래 꼭짓점은 (0, 0), 오른쪽 위 꼭짓점은 (w, h)에 있다. 
#직사각형의 경계선까지 가는 거리의 최솟값을 구하는 프로그램을 작성하시오.

#풀이
#x-0, y=0, w-x, h-x 
# #4가지 중 가장 작은 값이 직사각형의 경계선까지 가는 거리의 최소값이다


x,y,w,h= map(int,input().split())
print(min(x,y,w-x,h-y))
