N = int(input())
M = int(input())
x = int(input())
y = int(input())

if (N < M):
    short = N
    long = M
else:
    short = M
    long = N


y1 = long - y
x1 = short - x

if y1 <= y and y1 <= x and y1 <= x1:
    print(y1)
elif y <= y1 and y <= x and y <= x1:
    print(y)
elif x <= y1 and x <= y and x <= x1:
    print(x)
else:
    print(x1)
