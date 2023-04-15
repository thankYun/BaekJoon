5
def Hanoi1(N):
    if N==1:
        a.append(1)
    elif N == 2:
        a.append(1)
    else:
        a.append(a[N]+2)%3
    print(a)
    
# def Hanoi2(N):
#     if N==1:
#         return list(1,3)
#     elif N == 2:
#         return list(1,2)
#     elif N % 2 != 0:
#         RetHanoi=Hanoi(N-1)-int(2)
#     else:
#         print((inpNew1[0]+2)%3, (inpNew1[1]+2)%3)
#         return Hanoi2(N-1)


z=int(input())
count=0
for i in range(z):
    count += 2**i
print (count)


a=[]
b=[]
push=input()
if push == '!':
   print(Hanoi1(z))
# def HanoiOdd(N):
#     return Hanoi(N-1)

# def HanoiEven(N):
#     return Hanoi(N-1)


# for i in range(1,N):
#     inp=[]
#     Hanoi(i)
#     if N%2==0:
#         print('1 2')
#     else:
#         print('1 3')
