x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

dx = x2 - x1
dy = y2 - y1

if dx < 0:
    dx *= -1
if dy < 0:
    dy *= -1

if ((dx%2 == 0) and (dy%2 == 0))   or   (dx == dy)   or   ( (dx == 3) and (dy == 1) )   or   ( (dy == 3) and (dx == 1) ):
    print("YES")
else:
    print("NO")
