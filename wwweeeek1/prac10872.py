def ft(i):
    if i==0:
        return 1
    else:
        return i*ft(i-1)
    
print (ft(int(input())))