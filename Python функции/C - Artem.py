n = int (input())
 
mindel = n

def  MinDivisor(n):
    
     for k in range (2, n+1):
        if k**2 > n:
             return n
        elif n % k == 0:
            mindel = k
            return mindel
        
print (MinDivisor(n))
