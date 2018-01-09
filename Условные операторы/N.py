a = int(input())
b = int(input())

#if ((b//a == 0) and (b != 0)) or (b//a == -1):
    
    
if (a == 0):
    if (b == 0):
        print("INF")
    else:
        print("NO")

elif (b%a != 0):
    print("NO")
else:
    print(-b//a)
