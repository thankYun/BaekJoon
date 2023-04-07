# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

# 예를 들어, 서로 다른 9개의 자연수

# 3, 29, 38, 12, 57, 74, 40, 85, 61

# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

# 입력
# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.

# 출력
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.


# List_A=[3,29,38,12,57,74,40,85,61]
# List_A=list(map(int,input().split()))
# maximum=max(List_A)
# print(maximum)
# if List_A[0] == maximum:

#     print('1')
# elif List_A[1] == maximum:
#     print('2')
# elif List_A[2] == maximum:
#     print('3')
# elif List_A[3] == maximum:
#     print('4')
# elif List_A[4] == maximum:
#     print('5')
# elif List_A[5] == maximum:
#     print('6')
# elif List_A[6] == maximum:
#     print('7')
# elif List_A[7] == maximum:
#     print('8')
# else:
#     print('9')

# 계속되는 실패에 for 문을 풀어 실행하였는데도 틀렸다고 한다


# List_A.append(int(input()))
# 엔터 키 같은 경우 스플릿보다 for 문과 .append를 사용하는 것이 낫다는 말에 수정하였다.

# List_A = []

# for i in range(9):
#     List_A.append(int(input()))
# maximum=max(List_A)
# print(maximum)
# if List_A[0] == maximum:
#     print('1')
# elif List_A[1] == maximum:
#     print('2')
# elif List_A[2] == maximum:
#     print('3')
# elif List_A[3] == maximum:
#     print('4')
# elif List_A[4] == maximum:
#     print('5')
# elif List_A[5] == maximum:
#     print('6')
# elif List_A[6] == maximum:
#     print('7')
# elif List_A[7] == maximum:
#     print('8')
# else:
#     print('9')


    # 로 사용 한 결과 정답처리되었다.

# 이후 for 문으로 압축하였고

# List_A = []

# for i in range(9):
#     List_A.append(int(input()))
# maximum=max(List_A)
# print(maximum)
# for i in range(9):
#     if List_A[i] == maximum:
#         print(i+1)

List_A = []

for i in range(9):
    List_A.append(int(input()))
print(max(List_A))
for i in range(9):
    if List_A[i] == max(List_A):
        print(i+1)

#로 압축하였다