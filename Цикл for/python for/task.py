a = int(input())
b = int(input())

for k in range(a, (b+1)):
    f = (k // 1000)
    s = (k // 100) % 10
    t = (k // 10) % 10
    l = (k % 10)

    if (f == l) and (s == t):
        print(k)
