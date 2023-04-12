def Hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        Hanoi (N-1,a, c, b)
        Hanoi (1, a, b, c)
        Hanoi (N-1, b, a, c)

N=int(input())
count=0
if N <= 20:
    for i in range(N):
        count += 2**i
    print (count)
    Hanoi(N, 1, 2, 3)