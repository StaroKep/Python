def sh(n, k):
    if (k*(k+1))//2 < (n-1):
        return sh(n, k+1)
    else:
        return k

n = int(input())
print( sh(n, 0) )
