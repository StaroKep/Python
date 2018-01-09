x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
 
delta_x = x2 - x1
delta_y = y2 - y1
 
if ((delta_x >= -1) and (delta_x <= 1)) and ((delta_y >= -1) and (delta_y <= 1)):
    print("YES")
else:
    print("NO")
    
