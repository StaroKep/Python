n = int (input())
m = int (input())
k = int (input())
if n*m >= k and k % n == 0 or n*m >= k and k % m == 0:
    print ('YES')
else:
    print ('NO')
