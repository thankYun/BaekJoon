K = list(range(2,10001))
for i in range(len(K)-1, 0, -1):
    for j in range(2, int(K[i]**0.5)+1):
        if (K[i]) % j == 0:
            K.pop(i)
            break

print(K)