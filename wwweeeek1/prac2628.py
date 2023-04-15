X,Y=map(int,input().split())
T=int(input())
Xcut=[]
Ycut=[]
for i in range(T):
    Ty,Cut=map(int,input().split())
    if Ty==0:
        Ycut.append(Cut) 
    else:
        Xcut.append(Cut)

Xcut.sort()
Ycut.sort()
lX=[]
if len(Xcut)==0:
    lX.append(X)
elif len(Xcut)==1:
    lX.append(Xcut[0])
    lX.append(X-Xcut[0])
else:
    for i in range(len(Xcut)):
        if i==0:
            lX.append(Xcut[0])
        elif i==len(Xcut)-1:
            lX.append(X-Xcut[len(Xcut)-1])
            lX.append(Xcut[i]-Xcut[i-1])
        else:
            lX.append(Xcut[i]-Xcut[i-1])
lY=[]
if len(Ycut)==0:
    lY.append(Y)
elif len(Ycut)==1:
    lY.append(Ycut[0])
    lY.append(Y-Ycut[0])
else:
    for i in range(len(Ycut)):
        if i==0:
            lY.append(Ycut[0])
        elif i==len(Ycut)-1:
            lY.append(Y-Ycut[len(Ycut)-1])
            lY.append(Ycut[i]-Ycut[i-1])
        else:
            lY.append(Ycut[i]-Ycut[i-1])

print(max(lY)*max(lX))