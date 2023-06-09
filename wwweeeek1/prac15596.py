# 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.

# 작성해야 하는 함수는 다음과 같다.

# Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
# a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트 (0 ≤ a[i] ≤ 1,000,000, 1 ≤ n ≤ 3,000,000)
# 리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

#기본적으로 주어짐, 이것을 사용하여 하라는 것 같다.

#문제에서 보면 함수를 작성하시오 이기 때문에 함수만 작성하면 된다.
#a가 이미 리스트 형식으로 들어가져 있어 굳이 input을 사용 할 필요가 없다.
#이미 sum 함수를 사용한 적이 있기에 쉽게 풀 수 있었다.


def solve(a):
    return sum(a)