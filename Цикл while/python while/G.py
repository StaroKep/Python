x = int(input())
p = int(input())
y = int(input())



i = 0
while x < y:
    i += 1
    r = (x*p)//100
    k = ((x*p*100)//100)%100
    x += r + (k*0.01)
 
print(i)
