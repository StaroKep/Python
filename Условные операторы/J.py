x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

delta_x = x2 - x1
delta_y = y2 - y1

if (delta_x == delta_y) or (x1 == x2) or (y1 == y2):
    print("YES")
else:
    print("NO")
    
