N,goal=map(int,input().split())
A=list(map(int,input().split()))

base=[0]
count=0
for i in A:
    Floor=[]
    for j in base:
        Floor.append(j)             #i는 0+i=i로 아래줄에서 A에 들어가 있기 때문에
        Floor.append(i+j)           #(base 초기값이 0이므로) j 부터 시작하면 된다.
        if i+j==goal:
            count+=1
    base=Floor                      #base에 floor 정보를 업로드하고 floor을 초기화한다.
    del Floor
print (count)
