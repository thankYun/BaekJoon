import sys
t= int(input())

def A(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 3
    else:
        return A(n-3)+A(n-2)+A(n-1)
for i in range(N):
    print