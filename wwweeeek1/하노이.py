def Hanoi(N):
    #n 홀수일때
    if N%2 != 0:
        return Hanoi(N-2)
    #n 짝수일때
    else:
        return Hanoi(N-2)