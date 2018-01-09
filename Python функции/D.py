x = int(input())

def IsPrime(x):
    if x == 2:
        return True
    
    if (x % 2) == 0:
        return False

    i = 2
    while i <= int(x ** 0.5) + 1:
        if (x % i) == 0:
            return False
        i += 1
        
    return True

if IsPrime(x):
    print("YES")
else:
    print("NO")
