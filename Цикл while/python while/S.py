n = int(input())

t = n
i = 0
m = 0

while (n != 0):
    if (n == t):
        i += 1
        if i > m:
            m = i
    else:
        t = n
        i = 1
    n = int(input())

print(m)
