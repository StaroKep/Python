a = int(input())
m = 0
s = 0

while (a != 0):
    if (a > m):
        s = m
        m = a
    a = int(input())

print(s)
