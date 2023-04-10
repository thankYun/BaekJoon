A=list(range(1,int(input())+1))
count=0
for i in range (len(A)):
    B=list(str(A[i]))
    if len (B)<3:
        count+=1
    if len (B)==3:
        if int(B[1])-int(B[2])==int(B[0])-int(B[1]):
            count+=1
print(count)