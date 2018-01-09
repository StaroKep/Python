a = int(input())

def S(a):
    if a == 0:
        return a
    else:
        return a + S( int(input()) )

print( S(a) )
