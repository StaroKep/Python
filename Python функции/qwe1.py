def move (n, x, y):
    if n > 0:
        if (x + y) == 4:
            move(n, x, 2)
            move(n, 2, y)
        else:
            move(n-1, x, 6-x-y)
            print (n, x, y)
            move(n-1, 6-x-y, y)
n = int(input())
move(n,1,3)
