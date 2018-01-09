n = int(input())
m = int(input())

def ReduceFraction(n, m):
    if n < m:
        mi = n
    else:
        mi = m

    for i in range(mi, 2, -1):
        if ((n % i) == 0) and ((m % i) == 0):
            return (n//i, m//i)

    return (n, m)

k = ReduceFraction(n, m)
print(k[0], k[1], end="")
