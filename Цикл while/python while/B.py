n = int(input())
i = 2

while n % i != 0:
    if i < 10000:
        i += 1
    else:
        i = n
    
print(i)
