import sys
A, B, C = map(int,sys.stdin.readline().split())

def Divi(n):
    if n == 1:
        return A % C
    else:
        ndiv2 = Divi(n // 2)
        if n % 2 == 0:
            return (ndiv2 * ndiv2) % C
        else:
            return (ndiv2 * ndiv2 * A) % C

print(Divi(B))