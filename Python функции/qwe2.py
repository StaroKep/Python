def move (n, x, y):
    if n > 0:
        if (x + y) == 4:
            move (n-1, x, 2)
            print (n, x, y)
            move (n-1, 2, y)
        
n = int(input())
move(n,1,3)
