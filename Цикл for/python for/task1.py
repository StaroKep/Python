n = int(input())

if n == 1:
    m = 0
    x = 9
else:
    m = (10 ** (n-1)) - 1
    x = (10 ** n) - 1

for k in range(x, m, -2):
    print(k)
