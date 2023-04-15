def Hansu(N,x,y,num):
    if N==0:
        print(num)
    elif x<2**(N-1) and y<2**(N-1):
        num+=0
        return Hansu(N-1,x,y,num)
    elif x>=2**(N-1) and y<2**(N-1):
        num+=2**(2*N-2)
        return Hansu(N-1,x-2**(N-1),y,num)
    elif x<2**(N-1) and y>=2**(N-1):
        num+=2*2**(2*N-2)
        return Hansu(N-1,x,y-2**(N-1),num)
    else:
        num+=3*2**(2*N-2)
        return Hansu(N-1,x-2**(N-1),y-2**(N-1),num)


num=0
N,y,x =map(int,input().split())
Hansu(N,x,y,num)
