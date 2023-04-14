# from math import sqrt
# #Plate[1]에 전체 1 추가
# Test=[1,2,3]

# Test1 = list(map(lambda x: x+1, Test))
# print(Test1)

Plate=[[1,1,1],[1,1,0],[1,1,0]]
Plate[0] = list(map(lambda x: x+1, Plate[0]))

print(Plate)



