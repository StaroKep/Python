n = int(input())
s = 0

for k in range(2, n+1): 
    s += ((k-1) * k)

    print(k-1, '*', k, sep='', end='')
    if k != n:
        print('+', end='')
    else:
        print('=', end='')

print(s)
