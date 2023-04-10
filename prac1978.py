# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

#출력
#주어진 수들 중 소수의 개수를 출력한다.

#소수의 정의, 1과 자신만을 약수(?맞나? 용어가 생각이 안 난다.)로 갖는 수이다.
#시간이 될지 모르겠지만, n이 주어졌을 때 아래의 수를 map(int)로 받고 그 인자를 자연수로 나누어 나머지가 0인 자연수가 하나라도 있다면 제외시킨 후 len을 통해 세 보자

N=int(input())
Chart = list(map(int, input().split()))

  
a=0                                            
for i in range(len(Chart)):
    passs=0
    if Chart[i]==1:
        pass
    else:     
        for j in range(Chart[i]-2):        
            if Chart[i]%(j+2)==0:
                passs+=1
        if passs==0:
            a+=1
print (a)