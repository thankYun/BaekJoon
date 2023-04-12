# N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오. 
# 출력 형식에 맞춰서 출력하면 된다.

# N 인풋 후 프린트 *1~9

# insertNum=int(input())
# print(insertNum,'* 1 =',insertNum*1)
# print(insertNum,'* 2 =',insertNum*2)
# print(insertNum,'* 3 =',insertNum*3)
# print(insertNum,'* 4 =',insertNum*4)
# print(insertNum,'* 5 =',insertNum*5)
# print(insertNum,'* 6 =',insertNum*6)
# print(insertNum,'* 7 =',insertNum*7)
# print(insertNum,'* 8 =',insertNum*8)
# print(insertNum,'* 9 =',insertNum*9)

#로 풀었으나
#더 쉬운 방식이 있을 것 같아 list 형식으로 다시 제작하였다.
insertNum=str(input())
for i in range (1,10):
    print(insertNum,'*',i,'=',insertNum*i)
