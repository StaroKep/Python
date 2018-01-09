n = int(input())
m = int(input())
k = int(input())

if (n < m):
    var_min = n
else:
    var_min = m


if ( (k%n == 0) or (k%m == 0) ) and ( (k >= var_min) and (k <= (n*m-var_min)) ):
    print("YES")
else:
    print("NO")
