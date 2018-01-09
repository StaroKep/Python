k = int(input())

j = 0
n = 1
for i in range(1, k+1):
    if (j < n):
        print(n)
        j += 1
    else:
        n += 1
        print(n)
        j = 1
