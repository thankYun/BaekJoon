import sys


N = int(input())
count=0
address=[0]*N


def filt(y):
    for i in range (y):
        if address[y]==address[i] or abs(address[y]-address[i])==abs(y-i):
            return False

    return True
  
def nQ(x):
    global count
    if x==N:
        count+=1
        return
    else:
        for i in range(N):
            address[x]=i
            if filt(x):
                nQ(x+1)

nQ(0)
print(count)